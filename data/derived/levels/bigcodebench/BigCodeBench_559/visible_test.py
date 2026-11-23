from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        a = [1, 2, 3]
        b = [2, 3, 4]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertAlmostEqual(euclidean_distance, 1.732, places=3)
        self.assertTrue('A' in df.columns)
        self.assertTrue('B' in df.columns)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)

    def test_case_2(self):
        a = [1, 1, 1]
        b = [1, 1, 1]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertEqual(euclidean_distance, 0)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)

    def test_case_3(self):
        a = [0, 5, 10]
        b = [10, 5, 0]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertAlmostEqual(euclidean_distance, 14.142, places=3)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)
