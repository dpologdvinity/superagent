from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df, ax = task_func()
        self.assertEqual(len(df), 100)
        self.assertTrue(set(df['Category'].unique()).issubset(set(['a', 'b', 'c', 'd', 'e'])))
        self.assertTrue(df['Value'].min() >= 1)
        self.assertTrue(df['Value'].max() <= 100)
        self.assertEqual(ax.get_title(), 'Category Counts')

    def test_case_2(self):
        for num_rows in [10, 50, 100]:
            df, _ = task_func(num_rows=num_rows)
            self.assertEqual(len(df), num_rows)

    def test_case_3(self):
        with self.assertRaises(Exception):
            task_func(num_rows=0)

    def tearDown(self):
        plt.close('all')
