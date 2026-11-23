from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(task_func([[1, 1, 3], [4, 5, 6], [7, 8, 9]]), (1, 2))
    def test_case_2(self):
        self.assertEqual(task_func([[1, 1, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1]]), (1, 5))
    def test_case_3(self):
        self.assertEqual(task_func([[1, 1, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1], [2, 2, 2]]), (1, 5))
    def test_case_4(self):
        self.assertEqual(task_func([[1, 1, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1], [2, 2, 2], [3, 3, 3]]), (1, 5))
    def test_case_5(self):
        self.assertEqual(task_func([[1, 1, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]), (1, 5))
