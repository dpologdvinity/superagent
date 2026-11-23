from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing a standard UNIX-like path with '/' delimiter
        self.assertEqual(
            task_func("Docs/src/Scripts/temp", "/"),
            ["Docs", "src", "Scripts", "temp"],
        )
    def test_case_2(self):
        # Testing a standard Windows-like path with '\' delimiter
        self.assertEqual(
            task_func("Docs\\src\\Scripts\\temp", "\\"),
            ["Docs", "src", "Scripts", "temp"],
        )
    def test_case_3(self):
        # Testing an empty path string
        self.assertEqual(task_func("", "/"), [])
    def test_case_4(self):
        # Testing a path with invalid characters
        self.assertEqual(task_func("Docs/src/Scripts|temp", "/"), [])
    def test_case_5(self):
        # Testing a path with a different delimiter
        self.assertEqual(task_func("Docs|src|Scripts|temp", "|"), [])
    def test_case_6(self):
        # Handle leading and trailing delimiters
        self.assertEqual(task_func("/Docs/src/Scripts/", "/"), ["Docs", "src", "Scripts"])
    def test_case_7(self):
        # Test mixed delimiters given expected conversion
        self.assertEqual(
            task_func("Docs/src\\Scripts/temp", "\\"), ["Docs", "src", "Scripts", "temp"]
        )
        self.assertEqual(
            task_func("Docs/src\\Scripts/temp", "/"), ["Docs", "src", "Scripts", "temp"]
        )
