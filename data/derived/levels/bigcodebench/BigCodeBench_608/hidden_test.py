from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        # Common setup for generating DataFrame for testing
        self.df = pd.DataFrame({
            'A': list(range(0, 100, 10)) + [10, 60],
            'B': list(range(10, 110, 10)) + [20, 70],
            'C': list(range(20, 120, 10)) + [30, 80],
            'D': list(range(30, 130, 10)) + [40, 90],
            'E': list(range(40, 140, 10)) + [50, 100]
        })
    def test_case_1(self):
        tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
        modified_df, plots = task_func(self.df, tuples, 3)
        self.assertTrue(all(tuple(row) not in tuples for row in modified_df.to_numpy()))
        # Check the number of plots does not exceed min(n_plots, len(df.columns) // 2)
        expected_plot_count = min(3, len(self.df.columns) // 2)
        self.assertEqual(len(plots), expected_plot_count)
    def test_case_2(self):
        tuples = [(200, 200, 200, 200, 200), (300, 300, 300, 300, 300)]
        modified_df, plots = task_func(self.df, tuples, 2)
        self.assertEqual(len(modified_df), len(self.df))
        self.assertEqual(len(plots), 2)
    def test_case_3(self):
        tuples = []
        modified_df, plots = task_func(self.df, tuples, 1)
        self.assertEqual(len(modified_df), len(self.df))
        self.assertEqual(len(plots), 1)
    def test_case_4(self):
        tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
        modified_df, plots = task_func(self.df, tuples, 0)
        self.assertTrue(all(row not in modified_df.values for row in tuples))
        self.assertEqual(len(plots), 0)
    def test_case_5(self):
        tuples = [(10, 20, 30, 40, 50), (200, 200, 200, 200, 200)]
        modified_df, plots = task_func(self.df, tuples, 4)
        # Ensure the specific tuple is not in the DataFrame
        self.assertTrue((10, 20, 30, 40, 50) not in modified_df.values)
        # Check the number of plots does not exceed min(n_plots, len(df.columns) // 2)
        expected_plot_count = min(4, len(self.df.columns) // 2)
        self.assertEqual(len(plots), expected_plot_count)
