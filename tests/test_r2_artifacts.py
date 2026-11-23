import hashlib
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "results" / "runs" / "r2-pilot"
LEVELS = ROOT / "results" / "levels"


def _sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _rows():
    return [
        json.loads(line)
        for line in (RUN / "results.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def test_r2_artifacts_are_committed():
    for name in (
        "summary.json",
        "report.md",
        "results.jsonl",
        "manifest.json",
        "environment.json",
        "gpu_time.json",
        "endpoint.json",
        "bootstrap.json",
        "bootstrap.md",
        "COLAB_RUN.md",
        "colab_a100_vllm.ipynb",
        "README.md",
    ):
        assert (RUN / name).is_file(), f"missing {name}"
    assert len(list((RUN / "units").rglob("*.json"))) == 2700
    assert (RUN / "detector-smoothed" / "metrics.json").is_file()
    assert (RUN / "smoothing" / "wishes.jsonl").is_file()
    assert (RUN / "dry-run" / "summary.json").is_file()


def test_r2_run_is_complete_and_holds_out_nothing():
    summary = json.loads((RUN / "summary.json").read_text(encoding="utf-8"))
    manifest = json.loads((RUN / "manifest.json").read_text(encoding="utf-8"))
    assert summary["complete"] is True
    assert summary["completed_units"] == summary["expected_units"] == 2700
    assert summary["heldout_tasks_used"] == 0
    assert summary["tasks"] == 100
    assert summary["samples"] == 3
    assert summary["missing_units"] == {}
    assert manifest["status"] == "complete"
    assert manifest["units_completed"] == manifest["units_planned"] == 2700

    heldout = {
        task["key"]
        for task in (
            json.loads(line)
            for line in (LEVELS / "tasks.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
        if task["split"] == "heldout"
    }
    assert heldout
    assert not ({row["task_key"] for row in _rows()} & heldout)


def test_r2_summary_matches_the_unit_table():
    summary = json.loads((RUN / "summary.json").read_text(encoding="utf-8"))
    rows = _rows()
    assert len(rows) == 2700
    assert len({(r["condition"], r["task_key"], r["sample_index"]) for r in rows}) == 2700

    for condition, item in summary["conditions_summary"].items():
        selected = [row for row in rows if row["condition"] == condition]
        assert item["units"] == len(selected) == 300
        assert item["pass_at_1"] == pytest.approx(
            sum(bool(r["pass_at_1"]) for r in selected) / len(selected), abs=5e-4
        )
        assert item["pass_rate"] == pytest.approx(
            sum(bool(r["pass"]) for r in selected) / len(selected), abs=5e-4
        )


def test_r2_bootstrap_point_estimates_match_the_summary():
    bootstrap = json.loads((RUN / "bootstrap.json").read_text(encoding="utf-8"))
    summary = json.loads((RUN / "summary.json").read_text(encoding="utf-8"))
    assert bootstrap["results_sha256"] == _sha256(RUN / "results.jsonl")
    assert bootstrap["tasks"] == 100
    assert bootstrap["bootstrap"]["resamples"] == 2000
    assert bootstrap["bootstrap"]["seed"] == 20261121

    for contrast in bootstrap["contrasts"]:
        a = summary["conditions_summary"][contrast["a"]]["pass_at_1"]
        b = summary["conditions_summary"][contrast["b"]]["pass_at_1"]
        assert contrast["difference"] == pytest.approx(a - b, abs=1e-3)
        assert contrast["ci_low"] <= contrast["difference"] <= contrast["ci_high"]

    by_name = {item["name"]: item for item in bootstrap["contrasts"]}
    assert set(by_name) == {
        "B1-H0",
        "H2-H0",
        "H3-H0",
        "H4-H0",
        "H3-H2",
        "H3-H4",
        "DISCARD-H3",
        "B2-H0",
    }
    assert by_name["B1-H0"]["excludes_zero"] is True
    assert by_name["H3-H2"]["excludes_zero"] is False
    assert by_name["H3-H4"]["excludes_zero"] is False


def test_submitted_milestone_is_byte_identical():
    submitted = ROOT / "paper" / "milestone" / "submitted"
    assert _sha256(submitted / "main.tex") == (
        "760bf3807ed5b21d25542a2a4a68b890c7a3051811f433a5c3569d8c187bec2b"
    )
    assert _sha256(submitted / "main.pdf") == (
        "bb151114e8ec16e19af0b94be07fbc64fc53b1638ea364ffcf5c4798aa2ed668"
    )
    assert (ROOT / "paper" / "main.tex").is_file()
    assert (ROOT / "paper" / "main.pdf").is_file()
