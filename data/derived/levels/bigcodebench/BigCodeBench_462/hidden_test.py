from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with default parameters
        df, ax = task_func()
        self.assertEqual(len(df), 100)
        self.assertTrue(
            set(df["Category"].unique()).issubset(set(["a", "b", "c", "d", "e"]))
        )
        self.assertTrue(df["Value"].min() >= 1)
        self.assertTrue(df["Value"].max() <= 100)
        self.assertEqual(ax.get_title(), "Category Counts")
    def test_case_2(self):
        # Test num_rows
        for num_rows in [10, 50, 100]:
            df, _ = task_func(num_rows=num_rows)
            self.assertEqual(len(df), num_rows)
    def test_case_3(self):
        # Test edge case - 0 rows
        with self.assertRaises(Exception):
            task_func(num_rows=0)
    def test_case_4(self):
        # Test edge case - invalid num_rows
        with self.assertRaises(Exception):
            task_func(num_rows=-1)
    def test_case_5(self):
        # Test categories
        df, _ = task_func(categories=["x", "y", "z"])
        self.assertTrue(set(df["Category"].unique()).issubset(set(["x", "y", "z"])))
    def test_case_6(self):
        # Test edge case - single category
        df, _ = task_func(categories=["unique"])
        self.assertTrue(
            set(["unique"]).issubset(df["Category"].unique()),
            "Should work with a single category",
        )
    def test_case_7(self):
        # Test edge case - empty categories
        with self.assertRaises(Exception):
            task_func(categories=[])
    def test_case_8(self):
        # Test random seed
        df1, _ = task_func(random_seed=123)
        df2, _ = task_func(random_seed=123)
        df3, _ = task_func(random_seed=124)
        self.assertTrue(
            df1.equals(df2), "DataFrames should be identical with the same seed"
        )
        self.assertFalse(
            df1.equals(df3), "DataFrames should differ with different seeds"
        )
    def test_case_9(self):
        # Test visualization
        categories = ["x", "y", "z"]
        _, ax = task_func(num_rows=100, categories=categories, random_seed=42)
        ax_categories = [tick.get_text() for tick in ax.get_xticklabels()]
        self.assertListEqual(
            sorted(categories),
            sorted(ax_categories),
            "X-axis categories should match input categories",
        )
    def tearDown(self):
        plt.close("all")
