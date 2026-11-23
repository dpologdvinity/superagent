from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import pandas as pd
import unittest

class TestCases(unittest.TestCase):

    def test_random_reproducibility(self):
        report1 = task_func(['iPhone', 'iPad'], n_samples=50, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42)
        report2 = task_func(['iPhone', 'iPad'], n_samples=50, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42)
        pd.testing.assert_frame_equal(report1, report2)

    def test_number_of_rows(self):
        report = task_func(['iPhone', 'iPad'], n_samples=50, sales_lower=50, sales_upper=200)
        self.assertEqual(len(report), len(set(['iPhone', 'iPad'])))

    def test_sorting_by_profit(self):
        report = task_func(['iPhone', 'iPad'], sales_lower=50, sales_upper=200)
        self.assertTrue(report['Profit'].is_monotonic_decreasing)
