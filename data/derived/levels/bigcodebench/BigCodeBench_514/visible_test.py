from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df, ax = task_func([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.assertEqual(df.values.tolist(), [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D', 'E'])
        self.assertTrue(isinstance(ax, plt.Axes))

    def test_case_2(self):
        df, ax = task_func([[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [5, 15, 25, 35, 45]])
        self.assertEqual(df.values.tolist(), [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [5, 15, 25, 35, 45]])
        self.assertTrue(isinstance(ax, plt.Axes))

    def test_case_3(self):
        df, ax = task_func([[1, 1, 1, 1, 1]])
        self.assertEqual(df.values.tolist(), [[1, 1, 1, 1, 1]])
        self.assertTrue(isinstance(ax, plt.Axes))

    def tearDown(self):
        plt.close('all')
