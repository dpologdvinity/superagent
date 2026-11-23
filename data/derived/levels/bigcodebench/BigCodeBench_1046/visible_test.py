from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from datetime import datetime, timedelta

class TestCases(unittest.TestCase):
    """Test cases for the function."""

    def test_return_type(self):
        """Test if the function returns a Pandas DataFrame."""
        df_test = task_func('2023-01-01')
        self.assertIsInstance(df_test, pd.DataFrame)

    def test_correct_columns(self):
        """Test if the DataFrame has the correct columns: 'Employee' and 'Date'."""
        df_test = task_func('2023-01-01')
        self.assertListEqual(df_test.columns.tolist(), ['Employee', 'Date'])

    def test_date_range(self):
        """Test if the function generates the correct date range for 10 days."""
        start_date = '2023-01-01'
        df_test = task_func(start_date)
        end_date = (datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=9)).date()
        self.assertTrue(all(df_test['Date'] <= pd.Timestamp(end_date)))
