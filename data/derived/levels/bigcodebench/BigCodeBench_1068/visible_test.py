from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import sqlite3
import warnings

class TestCases(unittest.TestCase):
    """Test cases for task_func function."""

    def setUp(self):
        self.db_path = '/path/to/sqlite.db'
        self.query = 'SELECT * FROM table_name'
        self.mock_data = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})

    @patch('pandas.read_sql_query')
    @patch('sqlite3.connect')
    def test_successful_query(self, mock_connect, mock_read_sql):
        """
        Test task_func function for successful query execution.
        """
        mock_connect.return_value.__enter__.return_value = MagicMock()
        mock_read_sql.return_value = self.mock_data
        result = task_func(self.db_path, self.query)
        print(result)
        mock_connect.assert_called_with(self.db_path)
        mock_read_sql.assert_called_with(self.query, mock_connect.return_value.__enter__.return_value)
        self.assertTrue(result.equals(self.mock_data))

    @patch('pandas.read_sql_query')
    @patch('sqlite3.connect')
    def test_large_dataset_warning(self, mock_connect, mock_read_sql):
        """
        Test task_func function to check if it issues a warning for large datasets.
        """
        large_data = pd.DataFrame({'column1': range(10001)})
        mock_read_sql.return_value = large_data
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            task_func(self.db_path, self.query)
            self.assertEqual(len(w), 1)
            self.assertTrue('more than 10000 rows' in str(w[-1].message))

    @patch('pandas.read_sql_query')
    @patch('sqlite3.connect')
    def test_no_warning_for_small_dataset(self, mock_connect, mock_read_sql):
        """
        Test task_func function to ensure no warning for datasets smaller than 10000 rows.
        """
        mock_read_sql.return_value = self.mock_data
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            task_func(self.db_path, self.query)
            self.assertEqual(len(w), 0)
