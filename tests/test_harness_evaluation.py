from __future__ import annotations

from fakes import SOLUTION, make_task, make_unittest_task
from wishrec.harness.loop import evaluate_solution


def test_humaneval_style_hidden_suite_passes_and_fails():
    task = make_task()
    assert evaluate_solution(task, SOLUTION)["pass"] is True
    failed = evaluate_solution(task, "def add(a, b):\n    return a - b\n")
    assert failed["pass"] is False
    assert failed["bucket"] == "AssertionError"
    assert "AssertionError" in failed["output_tail"]


def test_bigcodebench_style_hidden_suite_uses_unittest():
    task = make_unittest_task()
    assert evaluate_solution(task, SOLUTION)["pass"] is True
    failed = evaluate_solution(task, "def add(a, b):\n    return None\n")
    assert failed["pass"] is False
    assert failed["bucket"] in ("AssertionError", "NonZeroExit")


def test_evaluation_does_not_need_or_expose_the_canonical_solution():
    task = make_task(canonical_solution="")
    assert task.canonical_solution == ""
    result = evaluate_solution(task, SOLUTION)
    assert result["pass"] is True
    assert "canonical" not in result
