import ast
import json

import pytest

from wishrec.parse import ParseError, parse_task

HUMANEVAL_ROW = {
    "task_id": "HumanEval/0",
    "entry_point": "add_one",
    "prompt": (
        "from typing import List\n"
        "\n"
        "\n"
        "def add_one(x: int) -> int:\n"
        '    """Add one to x, returning the result.\n'
        "    Note: x may be negative.\n"
        "    >>> add_one(1)\n"
        "    2\n"
        "    >>> add_one(-1)\n"
        "    0\n"
        '    """\n'
    ),
    "canonical_solution": "\n    return x + 1\n",
    "test": (
        "import numpy as np\n"
        "\n"
        "def assertion(out, exp, atol):\n"
        "    assert out == exp\n"
        "\n"
        "def check(candidate):\n"
        "    inputs = [[1], [2], [3], [4]]\n"
        "    results = [[2], [3], [4], [5]]\n"
        "    for i, (inp, exp) in enumerate(zip(inputs, results)):\n"
        "        assertion(candidate(*inp), exp, 0)\n"
    ),
}

MBPP_ROW = {
    "task_id": 7,
    "code": "\ndef double(x):\n    return x * 2\n",
    "prompt": "Return double the input. Note: x is positive.",
    "source_file": "test",
    "test_imports": [],
    "test_list": [
        "assert double(1) == 2",
        "assert double(2) == 4",
        "assert double(3) == 6",
    ],
    "test": (
        "import numpy as np\n"
        "def assertion(out, exp, atol):\n"
        "    assert out == exp\n"
        "inputs = [[1], [2], [3]]\n"
        "results = [[2], [4], [6]]\n"
        "for i, (inp, exp) in enumerate(zip(inputs, results)):\n"
        "    assertion(double(*inp), exp, 0)\n"
    ),
}

BCB_ROW = {
    "task_id": "BigCodeBench/0",
    "entry_point": "task_func",
    "complete_prompt": (
        "import numpy as np\n"
        "\n"
        "CONST = [1, 2]\n"
        "\n"
        "def task_func(x=1):\n"
        '    """Add x to a constant array.\n'
        "\n"
        "    Args:\n"
        "    - x (int): The value to add.\n"
        "\n"
        "    Returns:\n"
        "    numpy.ndarray: The shifted array.\n"
        "\n"
        "    Requirements:\n"
        "    - numpy\n"
        "\n"
        "    Example:\n"
        "    >>> task_func(1).tolist()\n"
        "    [2, 3]\n"
        '    """\n'
    ),
    "canonical_solution": "    return np.array(CONST) + x\n",
    "code_prompt": "import numpy as np\nCONST = [1, 2]\ndef task_func(x=1):\n",
    "test": (
        "import unittest\n"
        "class TestCases(unittest.TestCase):\n"
        "    def setUp(self):\n"
        "        self.x = 1\n"
        "    def test_a(self):\n"
        "        self.assertEqual(task_func(self.x).tolist(), [2, 3])\n"
        "    def test_b(self):\n"
        "        self.assertEqual(task_func(2).tolist(), [3, 4])\n"
        "    def test_c(self):\n"
        "        self.assertEqual(task_func(0).tolist(), [1, 2])\n"
        "    def test_d(self):\n"
        "        self.assertEqual(task_func(3).tolist(), [4, 5])\n"
    ),
    "doc_struct": json.dumps(
        {
            "description": ["Add x to a constant array.", "Args:", "- x (int): The value to add."],
            "notes": [],
            "params": [],
            "returns": ["numpy.ndarray: The shifted array."],
            "reqs": ["numpy"],
            "raises": ["ValueError if x is not an integer"],
            "examples": [">>> task_func(1).tolist()", "[2, 3]"],
        }
    ),
    "libs": json.dumps(["numpy"]),
}


def test_humaneval_parse():
    task = parse_task("humanevalplus", HUMANEVAL_ROW)
    assert task.key == "humanevalplus/HumanEval/0"
    assert task.entry_point == "add_one"
    assert task.fields["intent"] == "Add one to x, returning the result."
    assert ">>> add_one(1)" in task.fields["examples"]
    assert "x may be negative." in task.fields["constraints"]
    assert task.fields["signature_types"].startswith("from typing import List")
    assert "def add_one(x, )" not in task.fields["signature_untyped"]
    assert task.fields["signature_untyped"].startswith("def add_one(x)")
    assert task.fields_present["intent"]
    assert task.visible_asserts_count == 3
    assert task.visible_test.startswith("from solution import add_one\n")
    assert task.hidden_test.startswith("from solution import add_one\n")
    assert task.hidden_test.rstrip().endswith("check(add_one)")
    assert "inputs = [[1], [2], [3], [4]]" in task.hidden_test
    assert "inputs = [[1], [2], [3]]" in task.visible_test
    assert "numpy" in task.requirements
    assert task.stub.startswith("from typing import List")


def test_humaneval_ref_func_is_rejected():
    row = dict(HUMANEVAL_ROW)
    row["test"] = HUMANEVAL_ROW["test"].replace(
        "def check(candidate):",
        "def ref_func(x):\n    return x + 1\n\ndef check(candidate):",
    )
    with pytest.raises(ParseError, match="ref_func"):
        parse_task("humanevalplus", row)


def test_mbpp_parse():
    task = parse_task("mbppplus", MBPP_ROW)
    assert task.entry_point == "double"
    assert task.fields["intent"] == "Return double the input."
    assert "x is positive." in task.fields["constraints"]
    assert task.visible_asserts_count == 3
    assert task.visible_asserts.count("assert double") == 3
    assert task.visible_test.startswith("from solution import double\n")
    assert task.hidden_test.startswith("from solution import double\n")
    assert "candidate = double" in task.hidden_test
    assert task.stub.startswith("def double(x):")


def test_mbpp_requires_three_tests():
    row = dict(MBPP_ROW)
    row["test_list"] = ["assert double(1) == 2"]
    with pytest.raises(ParseError, match="three"):
        parse_task("mbppplus", row)


def test_bigcodebench_parse():
    task = parse_task("bigcodebench", BCB_ROW)
    assert task.entry_point == "task_func"
    assert task.fields["intent"] == "Add x to a constant array."
    assert "x (int)" in task.fields["signature_types"]
    assert "numpy.ndarray" in task.fields["signature_types"]
    assert ">>> task_func(1)" in task.fields["examples"]
    assert "numpy" in task.fields["constraints"]
    assert "ValueError" in task.fields["error_behaviour"]
    assert task.fields_present["error_behaviour"]
    assert task.visible_asserts_count == 3
    assert task.meta["visible_test_cases"] == ["test_a", "test_b", "test_c"]
    assert "test_d" not in task.visible_test
    assert "def setUp" in task.visible_test
    assert task.visible_test.startswith("from solution import task_func\n")
    assert task.hidden_test.startswith("from solution import task_func\n")
    assert "test_d" in task.hidden_test
    assert "CONST = [1, 2]" in task.stub
    assert "pass" in task.stub


def test_bigcodebench_requires_three_methods():
    row = dict(BCB_ROW)
    row["test"] = (
        "import unittest\n"
        "class TestCases(unittest.TestCase):\n"
        "    def test_a(self):\n"
        "        pass\n"
        "    def test_b(self):\n"
        "        pass\n"
    )
    with pytest.raises(ParseError, match="test_"):
        parse_task("bigcodebench", row)


def test_bigcodebench_visible_keeps_helpers_and_class_attributes():
    row = dict(BCB_ROW)
    row["test"] = (
        "import unittest\n"
        "LEVELS = [1, 2]\n"
        "def helper(value):\n"
        "    return value + 1\n"
        "class TestCases(unittest.TestCase):\n"
        "    EXPECTED = 2\n"
        "    def helper_method(self):\n"
        "        return self.EXPECTED\n"
        "    def test_a(self):\n"
        "        self.assertEqual(task_func(helper(self.EXPECTED)).tolist(), [4, 5])\n"
        "    def test_b(self):\n"
        "        self.assertEqual(task_func(0).tolist(), [1, 2])\n"
        "    def test_c(self):\n"
        "        self.assertEqual(task_func().tolist(), [2, 3])\n"
    )
    task = parse_task("bigcodebench", row)
    tree = ast.parse(task.visible_test)
    names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    assert "LEVELS" in names
    assert "helper" in names
    assert "EXPECTED" in names
    assert "helper_method" in task.visible_test
