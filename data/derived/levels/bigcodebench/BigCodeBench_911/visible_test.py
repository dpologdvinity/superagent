from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = task_func(['A', 'B', 'C'])
        self.assertEqual(result, 6)

    def test_case_2(self):
        result = task_func(['A', 'E', 'I'])
        self.assertEqual(result, 45)

    def test_case_3(self):
        result = task_func(['Z'])
        self.assertEqual(result, 26)
