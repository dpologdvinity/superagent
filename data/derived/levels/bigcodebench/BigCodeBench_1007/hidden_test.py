from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import requests
import pandas as pd
from unittest.mock import patch
class TestCases(unittest.TestCase):
    """Test cases for task_func."""
    @patch("requests.get")
    def test_valid_json(self, mock_get):
        """Test a valid JSON."""
        mock_get.return_value.json.return_value = [{"A": 1, "B": 3}, {"A": 2, "B": 4}]
        mock_get.return_value.status_code = 200
        df = task_func("https://example.com/data.json")
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertListEqual(df.columns.tolist(), ["A", "B"])
        self.assertListEqual(df["A"].tolist(), [1, 2])
        self.assertListEqual(df["B"].tolist(), [3, 4])
    @patch("requests.get")
    def test_empty_json(self, mock_get):
        """Test an empty JSON."""
        mock_get.return_value.json.return_value = []
        mock_get.return_value.status_code = 200
        df = task_func("https://example.com/empty.json")
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 0)
    @patch("requests.get")
    def test_invalid_json(self, mock_get):
        """Test an invalid JSON."""
        mock_get.return_value.json.side_effect = ValueError()
        with self.assertRaises(ValueError):
            task_func("https://example.com/invalid.json")
    @patch("requests.get")
    def test_large_json(self, mock_get):
        """Test a large JSON."""
        mock_get.return_value.json.return_value = [{"X": i} for i in range(1000)]
        mock_get.return_value.status_code = 200
        df = task_func("https://example.com/large.json")
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertListEqual(df["X"].tolist(), list(range(1000)))
    @patch("requests.get")
    def test_null_json(self, mock_get):
        """Test a JSON that is null."""
        mock_get.return_value.json.return_value = None
        mock_get.return_value.status_code = 200
        df = task_func("https://example.com/null.json")
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 0)
    @patch("requests.get")
    def test_system_error(self, mock_get):
        """Test a general error."""
        mock_get.side_effect = requests.RequestException
        with self.assertRaises(SystemError):
            task_func("https://example.com/data.json")
