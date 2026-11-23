from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with empty list
        result = task_func([])
        self.assertEqual(result, [])
    def test_case_2(self):
        # Testing with empty sublists
        result = task_func([[], [], []])
        self.assertEqual(result, [0, 0, 0])
        
    def test_case_3(self):
        # Testing with sublists of different lengths
        result = task_func([[1], [1, 2], [1, 2, 3]])
        self.assertEqual(result, [1, 5, 14])
    def test_case_4(self):
        # Testing with sublists containing the same element
        result = task_func([[1, 1, 1], [2, 2, 2, 2]])
        self.assertEqual(result, [14, 30])
        
    def test_case_5(self):
        # Testing with large sublists
        result = task_func([[1]*10, [2]*5])
        self.assertEqual(result, [385, 55])
