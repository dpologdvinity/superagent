from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_dataframe_structure(self):
        df, _ = task_func(10)
        self.assertEqual(df.shape, (10, 6))  # 10 rows, 6 columns
    def test_invalid_rows_input_negative(self):
        with self.assertRaises(ValueError):
            task_func(-1)
    def test_invalid_rows_input_zero(self):
        with self.assertRaises(ValueError):
            task_func(0)
    def test_invalid_rows_type(self):
        with self.assertRaises(ValueError):
            task_func("five")
    def test_stats_calculation(self):
        _, stats = task_func(10)
        for col_stats in stats.values():
            self.assertIn('mean', col_stats)
            self.assertIn('median', col_stats)
            
    def test_specific_stats_values(self):
        df, stats = task_func(10)
        for col in df.columns:
            expected_mean = df[col].mean()
            expected_median = df[col].median()
            self.assertAlmostEqual(stats[col]['mean'], expected_mean)
            self.assertAlmostEqual(stats[col]['median'], expected_median)
    def test_reproducibility_with_seed(self):
        df1, _ = task_func(10, seed=123)
        df2, _ = task_func(10, seed=123)
        pd.testing.assert_frame_equal(df1, df2)
