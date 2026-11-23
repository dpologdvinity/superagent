from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from unittest.mock import patch, mock_open
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    @patch("urllib.request.urlretrieve")
    @patch("os.remove")
    def test_sample_1(self, mock_remove, mock_urlretrieve):
        """Test that the function returns the correct DataFrame for a given JSON file."""
        url = "http://example.com/sample_1.json"
        sample_data = '[{"name": "Alice", "age": 25, "city": "New York"}, {"name": "Bob", "age": 30, "city": "San Francisco"}]'
        mock_urlretrieve.return_value = None
        with patch("builtins.open", mock_open(read_data=sample_data)):
            expected_df = pd.DataFrame(
                [
                    {"name": "Alice", "age": 25, "city": "New York"},
                    {"name": "Bob", "age": 30, "city": "San Francisco"},
                ]
            )
            result_df = task_func(url)
            pd.testing.assert_frame_equal(result_df, expected_df)
        mock_urlretrieve.assert_called_once_with(url, "downloaded_file.json")
        mock_remove.assert_called_once_with("downloaded_file.json")
    @patch("urllib.request.urlretrieve")
    @patch("os.remove")
    def test_sample_2(self, mock_remove, mock_urlretrieve):
        """Test that the function returns the correct DataFrame for a given JSON file."""
        url = "http://example.com/sample_2.json"
        sample_data = '[{"product": "Laptop", "price": 1000}, {"product": "Mouse", "price": 20}, {"product": "Keyboard", "price": 50}]'
        mock_urlretrieve.return_value = None
        with patch("builtins.open", mock_open(read_data=sample_data)):
            expected_df = pd.DataFrame(
                [
                    {"product": "Laptop", "price": 1000},
                    {"product": "Mouse", "price": 20},
                    {"product": "Keyboard", "price": 50},
                ]
            )
            result_df = task_func(url)
            pd.testing.assert_frame_equal(result_df, expected_df)
        mock_urlretrieve.assert_called_once_with(url, "downloaded_file.json")
        mock_remove.assert_called_once_with("downloaded_file.json")
    @patch("urllib.request.urlretrieve")
    @patch("os.remove")
    def test_empty_json(self, mock_remove, mock_urlretrieve):
        """Test that the function returns an empty DataFrame for an empty JSON file."""
        url = "http://example.com/empty.json"
        sample_data = "[]"
        mock_urlretrieve.return_value = None
        with patch("builtins.open", mock_open(read_data=sample_data)):
            expected_df = pd.DataFrame()
            result_df = task_func(url)
            pd.testing.assert_frame_equal(result_df, expected_df)
        mock_urlretrieve.assert_called_once_with(url, "downloaded_file.json")
    @patch("urllib.request.urlretrieve")
    def test_invalid_url(self, mock_urlretrieve):
        """Test that the function raises an exception when the URL is invalid."""
        url = "http://example.com/non_existent.json"
        mock_urlretrieve.side_effect = Exception("URL retrieval failed")
        with self.assertRaises(Exception):
            task_func(url)
        mock_urlretrieve.assert_called_once_with(url, "downloaded_file.json")
    @patch("urllib.request.urlretrieve")
    @patch("os.remove")
    def test_invalid_json(self, mock_remove, mock_urlretrieve):
        """Test that the function raises an exception when the JSON file is invalid."""
        url = "http://example.com/invalid.json"
        sample_data = "invalid json content"
        mock_urlretrieve.return_value = None
        with patch(
            "builtins.open", mock_open(read_data=sample_data)
        ), self.assertRaises(Exception):
            task_func(url)
        mock_urlretrieve.assert_called_once_with(url, "downloaded_file.json")
