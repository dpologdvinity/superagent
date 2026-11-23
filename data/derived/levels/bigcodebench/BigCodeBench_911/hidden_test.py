from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input: ["A", "B", "C"]
        # Expected Output: 6 (1 * 2 * 3)
        result = task_func(["A", "B", "C"])
        self.assertEqual(result, 6)
        
    def test_case_2(self):
        # Input: ["A", "E", "I"]
        # Expected Output: 45 (1 * 5 * 9)
        result = task_func(["A", "E", "I"])
        self.assertEqual(result, 45)
    def test_case_3(self):
        # Input: ["Z"]
        # Expected Output: 26
        result = task_func(["Z"])
        self.assertEqual(result, 26)
    def test_case_4(self):
        # Input: ["X", "Y", "Z"]
        # Expected Output: 24 * 25 * 26
        result = task_func(["X", "Y", "Z"])
        self.assertEqual(result, 24 * 25 * 26)
        
    def test_case_5(self):
        # Input: ["A", "A", "A"]
        # Expected Output: 1 (1 * 1 * 1)
        result = task_func(["A", "A", "A"])
        self.assertEqual(result, 1)
