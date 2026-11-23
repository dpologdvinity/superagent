"""Paired task-level bootstrap for the R2 pilot condition contrasts.

The pilot has three samples per (condition, task).  A task contributes one number per
condition---the mean of its sample-level pass@1 indicators---and conditions are paired
by task.  For a contrast ``a - b`` we resample the 100 tasks with replacement, take the
mean of the task-level differences in each resample, and report the percentile
interval.  Pairing keeps task difficulty fixed: the interval describes uncertainty about
the average difference over tasks, not the spread between unrelated task samples.

``pass_at_1`` is used when present (for B2 the runner records the first of its five
direct samples); ``pass`` is the fallback.  The pilot artifact is complete, so a
condition must provide the same task set as every other condition.

Run from the repository root:

    PYTHONPATH=src uv run python -m wishrec.harness.bootstrap \
        results/runs/r2-pilot/results.jsonl \
        --output results/runs/r2-pilot/bootstrap.json \
        --markdown results/runs/r2-pilot/bootstrap.md
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from .config import (
    atomic_write_json,
    atomic_write_text,
    read_jsonl,
    sha256_file,
    utc_now_iso,
)

#: Bootstrap settings fixed by the R3 ticket.
RESAMPLES = 2000
BOOTSTRAP_SEED = 20261121

#: Contrasts requested in the ticket, in report order.
CONTRASTS: tuple[tuple[str, str], ...] = (
    ("B1", "H0"),
    ("H2", "H0"),
    ("H3", "H0"),
    ("H4", "H0"),
    ("H3", "H2"),
    ("H3", "H4"),
    ("DISCARD", "H3"),
    ("B2", "H0"),
)


def load_task_means(
    results_path: Path,
) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, int]]]:
    """Read ``results.jsonl`` and aggregate each condition to task-level means.

    Returns ``(task_means, sample_counts)`` where ``task_means[condition][task]`` is the
    mean pass@1 over that task's samples and ``sample_counts[condition][task]`` is the
    number of samples behind it.
    """

    groups: dict[str, dict[str, list[float]]] = {}
    seen: set[tuple[str, str, int]] = set()
    for row in read_jsonl(results_path):
        try:
            condition = str(row["condition"])
            task = str(row["task_key"])
            sample = int(row["sample_index"])
            passed = row.get("pass_at_1", row.get("pass"))
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"{results_path}: malformed result row") from exc
        if passed is None:
            raise ValueError(f"{results_path}: row without pass/pass_at_1")
        key = (condition, task, sample)
        if key in seen:
            raise ValueError(f"{results_path}: duplicate unit {key}")
        seen.add(key)
        groups.setdefault(condition, {}).setdefault(task, []).append(float(bool(passed)))

    if not groups:
        raise ValueError(f"{results_path}: no result rows")
    task_means = {
        condition: {
            task: float(sum(values) / len(values)) for task, values in per_task.items()
        }
        for condition, per_task in groups.items()
    }
    sample_counts = {
        condition: {task: len(values) for task, values in per_task.items()}
        for condition, per_task in groups.items()
    }

    task_sets = {condition: set(per_task) for condition, per_task in task_means.items()}
    first = next(iter(task_sets.values()))
    for condition, task_set in task_sets.items():
        if task_set != first:
            missing = sorted(first - task_set)[:3]
            extra = sorted(task_set - first)[:3]
            raise ValueError(
                f"{results_path}: condition {condition} has a different task set "
                f"(missing {missing}, extra {extra})"
            )
    return task_means, sample_counts


def bootstrap_indices(tasks: int, resamples: int, seed: int) -> np.ndarray:
    """Draw the shared task index matrix used by every contrast."""

    if tasks <= 0:
        raise ValueError("no tasks to resample")
    if resamples <= 0:
        raise ValueError("resamples must be positive")
    rng = np.random.default_rng(seed)
    return rng.integers(0, tasks, size=(resamples, tasks))


def paired_interval(
    differences: np.ndarray,
    indices: np.ndarray,
    *,
    alpha: float = 0.05,
) -> tuple[float, float]:
    """Percentile bootstrap interval for the mean of paired task differences."""

    values = np.asarray(differences, dtype=float)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("differences must be a non-empty vector")
    boot = values[indices].mean(axis=1)
    low, high = np.quantile(boot, [alpha / 2.0, 1.0 - alpha / 2.0])
    return float(low), float(high)


def build_bootstrap(
    results_path: Path,
    *,
    resamples: int = RESAMPLES,
    seed: int = BOOTSTRAP_SEED,
    contrasts: tuple[tuple[str, str], ...] = CONTRASTS,
    alpha: float = 0.05,
) -> dict:
    """Compute condition means and paired task-level contrasts."""

    results_path = Path(results_path)
    task_means, sample_counts = load_task_means(results_path)
    conditions = sorted(task_means)
    missing = sorted({name for pair in contrasts for name in pair} - set(conditions))
    if missing:
        raise ValueError(f"contrasts reference unknown conditions: {missing}")

    tasks = sorted(task_means[conditions[0]])
    indices = bootstrap_indices(len(tasks), resamples, seed)
    condition_items = {
        condition: {
            "tasks": len(task_means[condition]),
            "units": int(sum(sample_counts[condition].values())),
            "pass_at_1": float(np.mean([task_means[condition][task] for task in tasks])),
        }
        for condition in conditions
    }
    contrast_items = []
    for a, b in contrasts:
        differences = np.array(
            [task_means[a][task] - task_means[b][task] for task in tasks]
        )
        low, high = paired_interval(differences, indices, alpha=alpha)
        difference = float(differences.mean())
        contrast_items.append(
            {
                "name": f"{a}-{b}",
                "a": a,
                "b": b,
                "difference": difference,
                "ci_low": low,
                "ci_high": high,
                "excludes_zero": bool(low > 0.0 or high < 0.0),
            }
        )

    sample_values = sorted(
        {count for per_task in sample_counts.values() for count in per_task.values()}
    )
    return {
        "format_version": 1,
        "generated_at": utc_now_iso(),
        "results": str(results_path),
        "results_sha256": sha256_file(results_path),
        "tasks": len(tasks),
        "samples_per_task": sample_values,
        "conditions": condition_items,
        "contrasts": contrast_items,
        "bootstrap": {
            "unit": "task",
            "paired": True,
            "statistic": "mean of task-level pass@1 differences",
            "resamples": resamples,
            "seed": seed,
            "interval": "percentile",
            "alpha": alpha,
        },
        "notes": [
            "Task-level means average each task's three samples; B2 uses pass@1, the "
            "first of its five direct samples.",
            "The same resample of the 100 tasks is reused for every contrast.",
            "The 300 held-out tasks are absent from the pilot results.",
        ],
    }


def render_markdown(summary: dict) -> str:
    """Render the bootstrap artifact as a short Markdown report."""

    lines = [
        "# R2 paired task-level bootstrap",
        "",
        f"- Generated: {summary['generated_at']}",
        f"- Source: `{summary['results']}` "
        f"(sha256 `{summary['results_sha256']}`)",
        f"- {summary['tasks']} tasks; samples per task "
        f"{summary['samples_per_task']}; {summary['bootstrap']['resamples']} resamples; "
        f"seed {summary['bootstrap']['seed']}",
        "",
        "| condition | pass@1 | tasks | units |",
        "| --- | --- | --- | --- |",
    ]
    for condition, item in summary["conditions"].items():
        lines.append(
            f"| {condition} | {item['pass_at_1'] * 100:.1f} | {item['tasks']} | "
            f"{item['units']} |"
        )
    lines.extend(
        [
            "",
            "| contrast | difference (pp) | 95% CI (pp) | excludes 0 |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in summary["contrasts"]:
        low = item["ci_low"] * 100.0
        high = item["ci_high"] * 100.0
        lines.append(
            f"| {item['name']} | {item['difference'] * 100:+.1f} | "
            f"[{low:+.1f}, {high:+.1f}] | "
            f"{'yes' if item['excludes_zero'] else 'no'} |"
        )
    lines.extend(["", "## Notes", "", *[f"- {note}" for note in summary["notes"]], ""])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", type=Path, help="results.jsonl from the R2 pilot")
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--markdown", type=Path, default=None)
    parser.add_argument("--resamples", type=int, default=RESAMPLES)
    parser.add_argument("--seed", type=int, default=BOOTSTRAP_SEED)
    args = parser.parse_args(argv)

    summary = build_bootstrap(
        args.results, resamples=args.resamples, seed=args.seed
    )
    output = args.output or args.results.with_name("bootstrap.json")
    atomic_write_json(output, summary)
    markdown = render_markdown(summary)
    markdown_path = args.markdown or output.with_suffix(".md")
    atomic_write_text(markdown_path, markdown)
    print(markdown)
    print(f"wrote {output} and {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "BOOTSTRAP_SEED",
    "CONTRASTS",
    "RESAMPLES",
    "bootstrap_indices",
    "build_bootstrap",
    "load_task_means",
    "main",
    "paired_interval",
    "render_markdown",
]
