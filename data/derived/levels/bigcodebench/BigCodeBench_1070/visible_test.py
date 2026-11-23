from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import random

class TestCases(unittest.TestCase):
    """Test cases for task_func function."""

    def test_dataframe_count(self):
        """Test number of dataframes returned."""
        random.seed(0)
        input_data = [['x', 'y'], ['a', 'b', 'c'], ['m']]
        dfs = task_func(input_data)
        self.assertEqual(len(dfs), len(input_data))

    def test_dataframe_columns(self):
        """Test each dataframe has correct columns."""
        random.seed(1)
        input_data = [['x', 'y'], ['a', 'b', 'c'], ['m']]
        dfs = task_func(input_data)
        for idx, df in enumerate(dfs):
            self.assertListEqual(list(df.columns), input_data[idx])

    def test_dataframe_values(self):
        """Test values in each dataframe column are from the POSSIBLE_VALUES list."""
        random.seed(2)
        input_data = [['x', 'y'], ['a', 'b', 'c'], ['m']]
        dfs = task_func(input_data)
        for df in dfs:
            for col in df.columns:
                self.assertTrue(all((val in POSSIBLE_VALUES for val in df[col].values)))
