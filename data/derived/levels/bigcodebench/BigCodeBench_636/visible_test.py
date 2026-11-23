from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df, ax = task_func(0)
        self.assertTrue(df.empty)
        self.assertEqual(len(ax.patches), 0)

    def test_case_2(self):
        df, ax = task_func(1)
        self.assertEqual(len(df), 1)
        self.assertEqual(len(ax.patches), 5)

    def test_case_3(self):
        df, ax = task_func(10)
        self.assertEqual(len(df), 10)
        self.assertEqual(len(ax.patches), 5)
