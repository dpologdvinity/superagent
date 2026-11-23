from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import random

class TestCases(unittest.TestCase):
    """Test cases for task_func."""

    def test_dataframe_creation(self):
        """
        Test if the function returns a pandas DataFrame.
        """
        random.seed(1)
        result = task_func()
        self.assertIsInstance(result, pd.DataFrame)

    def test_row_count(self):
        """
        Test if the DataFrame contains the correct number of rows.
        """
        random.seed(2)
        result = task_func()
        self.assertEqual(len(result), NUM_SAMPLES)

    def test_column_count(self):
        """
        Test if the DataFrame contains exactly two columns.
        """
        random.seed(3)
        result = task_func()
        self.assertEqual(len(result.columns), 2)
