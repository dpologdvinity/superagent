from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
# Importing the refined function from the refined_function.py file
import unittest
from unittest.mock import patch, Mock
import json
import requests
class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_valid_request(self, mock_get):
        mock_response = Mock()
        mock_response.text = '{"data": [1, 2, 3], "data_2": [4, 5, 6]}'
        mock_get.return_value = mock_response
        url = 'https://api.example.com/data'
        params = {'param1': 'value1'}
        df, ax = task_func(url, params)
        self.assertIsNotNone(df)
        self.assertIsNotNone(ax)
        # Check the content of the DataFrame
        self.assertTrue(df.equals(pd.DataFrame({"data": [1, 2, 3], "data_2": [4, 5, 6]})))
        # Check the correlation matrix
        corr_matrix = df.corr()
        # Check the data plotted on the heatmap
        for i in range(df.shape[1]):
            for j in range(df.shape[1]):
                self.assertEqual(ax.texts[i * df.shape[1] + j].get_text(), str(int(corr_matrix.iloc[i, j])))
    @patch('requests.get')
    def test_empty_response(self, mock_get):
        mock_response = Mock()
        mock_response.text = '{}'
        mock_get.return_value = mock_response
        url = 'https://api.example.com/empty_data'
        params = {'param1': 'value1'}
        with self.assertRaises(Exception):
            task_func(url, params)
    @patch('requests.get')
    def test_invalid_url(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException
        url = 'https://api.invalid.com/data'
        params = {'param1': 'value1'}
        with self.assertRaises(Exception):
            task_func(url, params)
    @patch('requests.get')
    def test_invalid_json_response(self, mock_get):
        mock_response = Mock()
        mock_response.text = 'Invalid JSON'
        mock_get.return_value = mock_response
        url = 'https://api.example.com/invalid_json'
        params = {'param1': 'value1'}
        with self.assertRaises(Exception):
            task_func(url, params)
    @patch('requests.get')
    def test_valid_request_with_no_params(self, mock_get):
        mock_response = Mock()
        mock_response.text = '{"data": [1, 2, 3, 4, 5]}'
        mock_get.return_value = mock_response
        url = 'https://api.example.com/data'
        df, ax = task_func(url, {})
        self.assertIsNotNone(df)
        self.assertIsNotNone(ax)
    @patch('requests.get')
    def test_plot_attributes(self, mock_get):
        # Test attributes of the plot
        mock_response = Mock()
        mock_response.text = '{"id": [1, 2, 3, 4, 5], "user": [6, 7, 8, 9, 10]}'
        mock_get.return_value = mock_response
        url = 'https://api.example.com/data'
        params = {'param1': 'value1'}
        df, ax = task_func(url, params)
        self.assertTrue(hasattr(ax, 'get_xlabel'))
        self.assertTrue(hasattr(ax, 'get_ylabel'))
        self.assertTrue(hasattr(ax, 'get_title'))
