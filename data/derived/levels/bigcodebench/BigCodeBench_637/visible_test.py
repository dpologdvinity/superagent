from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df, ax = task_func(10)
        self.assertEqual(df.shape, (10, 5))
        self.assertEqual(ax.get_title(), 'Course-wise Average and Passing Grade Counts')

    def test_case_2(self):
        df, ax = task_func(50)
        self.assertEqual(df.shape, (50, 5))
        self.assertEqual(ax.get_title(), 'Course-wise Average and Passing Grade Counts')

    def test_case_3(self):
        df, ax = task_func(100)
        self.assertEqual(df.shape, (100, 5))
        self.assertEqual(ax.get_title(), 'Course-wise Average and Passing Grade Counts')
