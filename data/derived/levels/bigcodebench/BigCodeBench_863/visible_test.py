from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = task_func([])
        self.assertEqual(result, [])

    def test_case_2(self):
        result = task_func([[], [], []])
        self.assertEqual(result, [0, 0, 0])

    def test_case_3(self):
        result = task_func([[1], [1, 2], [1, 2, 3]])
        self.assertEqual(result, [1, 5, 14])
