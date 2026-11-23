from __future__ import annotations

import json

import numpy as np
import pytest

from wishrec.harness.bootstrap import (
    CONTRASTS,
    build_bootstrap,
    load_task_means,
    main,
)


def _row(condition, task, sample, *, passed, pass_at_1=None):
    return {
        "condition": condition,
        "task_key": task,
        "sample_index": sample,
        "pass": passed,
        "pass_at_1": passed if pass_at_1 is None else pass_at_1,
        "status": "complete",
    }


def _write_results(tmp_path, rows, *, name="results.jsonl"):
    path = tmp_path / name
    path.write_text(
        "\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8"
    )
    return path


def _rows():
    rows = []
    for task in ("pilot/a", "pilot/b", "pilot/c"):
        for sample in range(3):
            rows.append(_row("B1", task, sample, passed=True))
            rows.append(_row("H0", task, sample, passed=False))
            rows.append(
                _row(
                    "B2",
                    task,
                    sample,
                    passed=True,
                    pass_at_1=task == "pilot/a" and sample == 0,
                )
            )
            # The remaining conditions only need to exist so the CLI can evaluate the
            # full ticket contrast list.
            rows.append(_row("H2", task, sample, passed=False))
            rows.append(_row("H3", task, sample, passed=True))
            rows.append(_row("H4", task, sample, passed=False))
            rows.append(_row("DISCARD", task, sample, passed=False))
    return rows


def test_task_means_average_samples_and_use_pass_at_1(tmp_path):
    results = _write_results(tmp_path, _rows())
    task_means, sample_counts = load_task_means(results)

    assert task_means["B1"] == {"pilot/a": 1.0, "pilot/b": 1.0, "pilot/c": 1.0}
    assert task_means["H0"] == {"pilot/a": 0.0, "pilot/b": 0.0, "pilot/c": 0.0}
    assert task_means["B2"]["pilot/a"] == pytest.approx(1 / 3)
    assert task_means["B2"]["pilot/b"] == 0.0
    assert sample_counts["B2"]["pilot/a"] == 3


def test_bootstrap_contrasts_are_paired_and_deterministic(tmp_path):
    results = _write_results(tmp_path, _rows())
    summary = build_bootstrap(
        results, resamples=200, seed=7, contrasts=(("B1", "H0"), ("B2", "H0"))
    )

    assert summary["tasks"] == 3
    assert summary["conditions"]["B2"]["pass_at_1"] == pytest.approx(1 / 9)
    first, second = summary["contrasts"]
    assert first["name"] == "B1-H0"
    assert first["difference"] == 1.0
    assert (first["ci_low"], first["ci_high"]) == (1.0, 1.0)
    assert first["excludes_zero"] is True
    assert second["name"] == "B2-H0"
    assert second["difference"] == pytest.approx(1 / 9)
    assert second["excludes_zero"] is False
    assert summary["bootstrap"]["paired"] is True

    again = build_bootstrap(
        results, resamples=200, seed=7, contrasts=(("B1", "H0"), ("B2", "H0"))
    )
    assert again["contrasts"] == summary["contrasts"]


def test_bootstrap_requires_a_shared_task_set(tmp_path):
    rows = _rows()
    rows = [row for row in rows if not (row["condition"] == "B2" and row["task_key"] == "pilot/c")]
    results = _write_results(tmp_path, rows)
    with pytest.raises(ValueError, match="different task set"):
        load_task_means(results)


def test_bootstrap_rejects_duplicate_units(tmp_path):
    rows = _rows()
    rows.append(rows[0])
    results = _write_results(tmp_path, rows)
    with pytest.raises(ValueError, match="duplicate unit"):
        load_task_means(results)


def test_bootstrap_cli_writes_json_and_markdown(tmp_path):
    results = _write_results(tmp_path, _rows())
    output = tmp_path / "bootstrap.json"
    markdown = tmp_path / "bootstrap.md"
    code = main(
        [
            str(results),
            "--output",
            str(output),
            "--markdown",
            str(markdown),
            "--resamples",
            "50",
        ]
    )
    assert code == 0
    saved = json.loads(output.read_text(encoding="utf-8"))
    assert saved["results"] == str(results)
    assert [item["name"] for item in saved["contrasts"]] == [
        f"{a}-{b}" for a, b in CONTRASTS
    ]
    assert "paired task-level bootstrap" in markdown.read_text(encoding="utf-8")


def test_bootstrap_indices_are_shared_across_contrasts(tmp_path):
    # Two contrasts observe the same resample matrix, so identical difference vectors
    # must produce identical intervals.
    from wishrec.harness.bootstrap import bootstrap_indices, paired_interval

    indices = bootstrap_indices(10, 100, 20261121)
    differences = np.linspace(-1.0, 1.0, 10)
    assert paired_interval(differences, indices) == paired_interval(
        differences, indices
    )
