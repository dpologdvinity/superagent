"""Resumable smoke/pilot runner.

R1 never calls the runner against a GPU endpoint; the ticket's tests use the same code
with a local fake endpoint.  R2 runs ``python -m wishrec.harness.runner pilot`` against the
operator's vLLM server, one unit per (condition, task, sample), with complete per-unit
traces and cached results so an interrupted GPU session can resume.

The runner never uses the held-out split for a pilot.  ``pilot`` selects only R0's disjoint
100-task pilot split; ``--split heldout`` is refused.
"""

from __future__ import annotations

import argparse
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from .conditions import CONDITION_ORDER, Condition, resolve_conditions
from .config import (
    GENERATOR_SEED,
    QUESTION_BUDGET,
    TURN_CAP,
    atomic_write_json,
    atomic_write_text,
    environment_info,
    frontier_config,
    generator_config,
    git_info,
    harness_source_hash,
    sha256_text,
    utc_now_iso,
)
from .detector import load_default_detector
from .llm import LLMClient
from .loop import run_unit
from .models import Task, load_manifest, load_tasks

DEFAULT_OUTPUT_DIR = Path("results/runs")
CONDITION_SPLIT_NOTE = {"B1": "L0", "B2": "direct 5 samples", "B3": "direct frontier"}


def sibling_contexts(tasks: list[Task], *, k: int = 5) -> dict[str, list[dict]]:
    """Five target-excluding siblings with canonical code and example doctests.

    The context is informational, like nearby functions in a codebase.  It comes only from
    committed fields and the derived canonical solutions; no hidden test is ever included.
    """
    by_source: dict[str, list[Task]] = {}
    for task in tasks:
        by_source.setdefault(task.source, []).append(task)
    contexts: dict[str, list[dict]] = {}
    for target in tasks:
        pool = sorted(
            [task for task in by_source[target.source] if task.key != target.key],
            key=lambda task: task.key,
        )
        if not pool:
            contexts[target.key] = []
            continue
        start = int(sha256_text(target.key)[:8], 16) % len(pool)
        chosen: list[Task] = []
        for offset in range(len(pool)):
            candidate = pool[(start + offset) % len(pool)]
            if candidate.key not in {task.key for task in chosen}:
                chosen.append(candidate)
            if len(chosen) >= k:
                break
        contexts[target.key] = [
            {
                "key": task.key,
                "entry_point": task.entry_point,
                "code": task.canonical_solution.strip(),
                "doctests": _doctest_block(task),
            }
            for task in chosen
        ]
    return contexts


def _doctest_block(task: Task) -> str:
    examples = str(task.fields.get("examples") or "").strip()
    if examples:
        return examples
    if task.visible_asserts.strip():
        return (
            "# visible assertions from a sibling task\n"
            + "\n".join(f"# {line}" for line in task.visible_asserts.splitlines())
        )
    return ""


def unit_key(condition: Condition, task: Task, sample_index: int) -> str:
    return f"{condition.name}/{sample_index}/{task.key}"


def unit_path(run_dir: Path, condition: Condition, task: Task, sample_index: int) -> Path:
    safe_key = task.key.replace("/", "__")
    return run_dir / "units" / condition.name / str(sample_index) / f"{safe_key}.json"


def _config_hash(config: dict) -> str:
    return sha256_text(json.dumps(config, sort_keys=True, ensure_ascii=False))


def build_config(
    tasks: list[Task],
    conditions: list[Condition],
    samples: int,
    *,
    run_id: str,
    seed: int = GENERATOR_SEED,
) -> dict:
    return {
        "run_id": run_id,
        "task_keys": [task.key for task in tasks],
        "conditions": [condition.name for condition in conditions],
        "sample_indices": list(range(max(1, samples))),
        "seed": seed,
        "turn_cap": TURN_CAP,
        "question_budget": QUESTION_BUDGET,
        "generator": generator_config().safe_identity,
        "frontier": frontier_config().safe_identity,
        "harness_source_hash": harness_source_hash(),
        "condition_descriptions": {
            condition.name: condition.description for condition in conditions
        },
    }


def _compact(result: dict) -> dict:
    return {
        "condition": result["condition"],
        "task_key": result["task_key"],
        "sample_index": result.get("sample_index", 0),
        "pass": bool(result.get("pass")),
        "pass_at_1": bool(result.get("pass_at_1", result.get("pass"))),
        "bucket": result.get("bucket"),
        "turns": result.get("turns", 0),
        "questions": result.get("questions", 0),
        "turn_cap_hit": result.get("turn_cap_hit", False),
        "api_error": result.get("api_error", ""),
        "duration_s": result.get("duration_s", 0.0),
        "totals": result.get("totals", {}),
    }


def summarise(run_dir: Path, config: dict) -> tuple[dict, str]:
    conditions = config["conditions"]
    summaries = {}
    total_units = 0
    for condition_name in conditions:
        units = []
        directory = run_dir / "units" / condition_name
        if directory.exists():
            allowed_tasks = set(config.get("task_keys", []))
            allowed_samples = set(config.get("sample_indices", []))
            for path in sorted(directory.rglob("*.json")):
                try:
                    unit = json.loads(path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError):
                    continue
                if allowed_tasks and unit.get("task_key") not in allowed_tasks:
                    continue
                if allowed_samples and unit.get("sample_index", 0) not in allowed_samples:
                    continue
                units.append(unit)
        total_units += len(units)
        passes = sum(1 for unit in units if unit.get("pass"))
        pass_at_1 = sum(
            1 for unit in units if unit.get("pass_at_1", unit.get("pass"))
        )
        buckets: dict[str, int] = {}
        for unit in units:
            if unit.get("pass"):
                continue
            bucket = str(unit.get("bucket", "unknown"))
            buckets[bucket] = buckets.get(bucket, 0) + 1
        tokens = {
            "input": sum(
                int(unit.get("totals", {}).get("input_tokens", 0) or 0) for unit in units
            ),
            "output": sum(
                int(unit.get("totals", {}).get("output_tokens", 0) or 0) for unit in units
            ),
        }
        summaries[condition_name] = {
            "units": len(units),
            "passes": passes,
            "pass_rate": round(passes / len(units), 4) if units else None,
            "pass_at_1": round(pass_at_1 / len(units), 4) if units else None,
            "avg_turns": round(
                sum(int(unit.get("turns", 0) or 0) for unit in units) / len(units), 2
            )
            if units
            else None,
            "avg_questions": round(
                sum(int(unit.get("questions", 0) or 0) for unit in units) / len(units), 2
            )
            if units
            else None,
            "turn_cap_units": sum(1 for unit in units if unit.get("turn_cap_hit")),
            "buckets": buckets,
            "tokens": tokens,
        }
    summary = {
        "run_id": config.get("run_id"),
        "generated_at": utc_now_iso(),
        "config_hash": _config_hash(config),
        "conditions": summaries,
        "units": total_units,
        "task_keys": config.get("task_keys", []),
    }
    lines = [
        "# Harness run",
        "",
        f"- Run: `{config.get('run_id')}`",
        f"- Tasks: {len(config.get('task_keys', []))}",
        f"- Conditions: {', '.join(conditions)}",
        f"- Units: {total_units}",
        "",
        "| condition | passed | pass@1 | avg turns | avg questions | cap hits | buckets |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for condition_name in conditions:
        item = summaries[condition_name]
        buckets = ", ".join(f"{key}:{value}" for key, value in sorted(item["buckets"].items()))
        lines.append(
            f"| {condition_name} | {item['passes']}/{item['units']} | "
            f"{item['pass_at_1']} | {item['avg_turns']} | {item['avg_questions']} | "
            f"{item['turn_cap_units']} | {buckets or '—'} |"
        )
    lines.extend(
        [
            "",
            "Only the development split may be used for a pilot; held-out results belong to",
            "the final R3 report.",
        ]
    )
    return summary, "\n".join(lines) + "\n"


def execute_unit(
    task: Task,
    condition: Condition,
    *,
    run_id: str,
    sample_index: int,
    seed: int,
    detector,
    siblings: list[dict] | None,
) -> dict:
    started = time.monotonic()
    config = frontier_config() if condition.b3 else generator_config()
    client = LLMClient(
        config,
        seed=seed + sample_index,
        purpose="b3" if condition.b3 else "generator",
    )
    try:
        result = run_unit(
            task,
            condition,
            client,
            detector=detector,
            siblings=siblings,
            seed=seed + sample_index,
            run_id=run_id,
            sample_index=sample_index,
        )
    except Exception as exc:  # noqa: BLE001 - a failed unit is an artifact
        result = {
            "condition": condition.name,
            "task_key": task.key,
            "source": task.source,
            "source_task_id": task.source_task_id,
            "entry_point": task.entry_point,
            "sample_index": sample_index,
            "seed": seed + sample_index,
            "run_id": run_id,
            "pass": False,
            "bucket": "HarnessError",
            "turns": 0,
            "questions": 0,
            "detector_questions": [],
            "follow_up_questions": [],
            "solution_written": False,
            "final_solution": "",
            "evaluation": {},
            "self_check": None,
            "llm_calls": [],
            "trace_events": [
                {"event": "harness_error", "error": f"{type(exc).__name__}: {exc}"}
            ],
            "messages": [],
            "tools": {},
            "totals": {},
            "api_error": f"{type(exc).__name__}: {exc}",
            "status": "error",
        }
    result["condition"] = condition.name
    result["task_key"] = task.key
    result["run_id"] = run_id
    result["sample_index"] = sample_index
    result["duration_s"] = round(time.monotonic() - started, 3)
    return result


def run_units(
    *,
    tasks: list[Task],
    conditions: list[Condition],
    run_id: str,
    output_dir: Path,
    samples: int = 1,
    workers: int = 1,
    seed: int = GENERATOR_SEED,
    force: bool = False,
    progress=print,
) -> dict:
    if not tasks:
        raise ValueError("no tasks selected")
    if not conditions:
        raise ValueError("no conditions selected")
    config = build_config(tasks, conditions, samples, run_id=run_id, seed=seed)
    digest = _config_hash(config)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = output_dir / "manifest.json"
    if manifest_path.exists() and not force:
        old = json.loads(manifest_path.read_text(encoding="utf-8"))
        if old.get("config_hash") != digest:
            raise RuntimeError(
                f"run {run_id!r} exists with config {old.get('config_hash')} != {digest}; "
                "rerun with --force"
            )

    level_manifest = load_manifest()
    detector = None
    if any(condition.targeted for condition in conditions):
        detector = load_default_detector()
    sibling_map = (
        sibling_contexts(tasks) if any(condition.siblings for condition in conditions) else {}
    )

    planned = [
        (condition, task, sample_index)
        for condition in conditions
        for task in tasks
        for sample_index in range(max(1, samples))
    ]
    manifest = {
        "run_id": run_id,
        "created_at": utc_now_iso(),
        "git": git_info(),
        "environment": environment_info(),
        "level_manifest_sha256": sha256_text(
            json.dumps(level_manifest, sort_keys=True)
        ),
        "config": config,
        "config_hash": digest,
        "planned_units": len(planned),
        "level": level_manifest.get("phase", "R0"),
        "status": "running",
    }
    atomic_write_json(manifest_path, manifest)

    started = time.monotonic()
    completed = 0
    skipped = 0
    errors: list[str] = []
    results: list[dict] = []

    def job(condition: Condition, task: Task, sample_index: int):
        path = unit_path(output_dir, condition, task, sample_index)
        if path.exists() and not force:
            try:
                existing = json.loads(path.read_text(encoding="utf-8"))
                if (
                    existing.get("status") == "complete"
                    and existing.get("config_hash") == digest
                ):
                    return "skipped", existing
            except (OSError, json.JSONDecodeError):
                pass
        result = execute_unit(
            task,
            condition,
            run_id=run_id,
            sample_index=sample_index,
            seed=seed,
            detector=detector,
            siblings=sibling_map.get(task.key),
        )
        result["config_hash"] = digest
        result["created_at"] = utc_now_iso()
        atomic_write_json(path, result)
        return "done", result

    with ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
        futures = {
            executor.submit(job, condition, task, sample_index): (
                condition,
                task,
                sample_index,
            )
            for condition, task, sample_index in planned
        }
        for future in as_completed(futures):
            condition, task, sample_index = futures[future]
            try:
                status, result = future.result()
            except Exception as exc:  # noqa: BLE001
                status = "error"
                result = None
                errors.append(f"{condition.name}/{task.key}/{sample_index}: {exc}")
            completed += 1
            if status == "skipped":
                skipped += 1
                progress(
                    f"[{completed}/{len(planned)}] skip {condition.name} "
                    f"{task.key} sample={sample_index}"
                )
                continue
            if result is None:
                progress(f"[{completed}/{len(planned)}] ERROR {condition.name} {task.key}")
                continue
            results.append(result)
            if result.get("api_error"):
                errors.append(
                    f"{condition.name}/{task.key}/{sample_index}: {result['api_error']}"
                )
            progress(
                f"[{completed}/{len(planned)}] {condition.name} {task.key} "
                f"sample={sample_index} {'PASS' if result.get('pass') else 'fail'} "
                f"turns={result.get('turns')} q={result.get('questions')}"
            )

    summary, report = summarise(output_dir, config)
    atomic_write_json(output_dir / "summary.json", summary)
    atomic_write_text(output_dir / "report.md", report)
    atomic_write_text(
        output_dir / "results.jsonl",
        "\n".join(json.dumps(_compact(result), sort_keys=True) for result in results)
        + ("\n" if results else ""),
    )
    manifest.update(
        {
            "finished_at": utc_now_iso(),
            "status": "complete",
            "units_completed": summary["units"],
            "units_skipped": skipped,
            "errors": errors[:50],
            "duration_s": round(time.monotonic() - started, 1),
        }
    )
    atomic_write_json(manifest_path, manifest)
    progress(report)
    return {"manifest": manifest, "summary": summary, "output_dir": str(output_dir)}


def _task_selection(args) -> list[Task]:
    if args.split == "heldout":
        raise SystemExit("refusing to pilot on the held-out split; that split belongs to R3")
    return load_tasks(
        split=args.split,
        keys=args.tasks,
        limit=args.limit,
    )


def _add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--conditions", nargs="*", default=None)
    parser.add_argument("--tasks", nargs="*", default=None, help="explicit task keys")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--samples", type=int, default=1)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--seed", type=int, default=GENERATOR_SEED)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the planned units and endpoint identity without calling the endpoint",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    smoke = subparsers.add_parser("smoke", help="small development-split smoke run")
    _add_common(smoke)
    smoke.add_argument("--split", default="evolution")
    pilot = subparsers.add_parser("pilot", help="R2 100-task development pilot")
    _add_common(pilot)
    pilot.set_defaults(split="pilot", samples=3)
    run = subparsers.add_parser("run", help="explicit split/conditions run")
    _add_common(run)
    run.add_argument("--split", default="pilot")
    args = parser.parse_args(argv)

    tasks = _task_selection(args)
    conditions = resolve_conditions(args.conditions)
    if args.command == "pilot" and len(tasks) != 100 and args.tasks is None and args.limit is None:
        raise SystemExit(f"pilot expects 100 tasks, found {len(tasks)}")
    output_dir = args.output or (DEFAULT_OUTPUT_DIR / args.run_id)
    config = build_config(tasks, conditions, args.samples, run_id=args.run_id, seed=args.seed)
    if args.dry_run:
        print(json.dumps({"config": config, "units": len(tasks) * len(conditions) * max(1, args.samples)}, indent=2))
        return 0
    run_units(
        tasks=tasks,
        conditions=conditions,
        run_id=args.run_id,
        output_dir=output_dir,
        samples=args.samples,
        workers=args.workers,
        seed=args.seed,
        force=args.force,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_OUTPUT_DIR",
    "build_config",
    "execute_unit",
    "main",
    "run_units",
    "sibling_contexts",
    "summarise",
    "unit_key",
    "unit_path",
]
