from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, Mock
import os
import json

class TestCases(unittest.TestCase):

    def tearDown(self):
        for filename in ('PREFIX_data.json', 'PREFIX_empty.json', 'PREFIX_temp.json'):
            if os.path.exists(filename):
                os.remove(filename)

    @patch('requests.get')
    def test_successful_data_fetch(self, mock_get):
        mock_data = {'name': 'test', 'value': 123}
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_data)
        api_url = 'https://fakeapi.com/'
        endpoint = 'data'
        prefix = 'PREFIX_'
        expected_filename = prefix + endpoint + '.json'
        result = task_func(api_url, endpoint, prefix)
        self.assertEqual(result, expected_filename)
        with open(result, 'r') as file:
            data = json.load(file)
        self.assertEqual(data, mock_data)

    @patch('requests.get')
    def test_empty_response_handling(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {})
        api_url = 'https://fakeapi.com/'
        endpoint = 'empty'
        prefix = 'PREFIX_'
        expected_filename = prefix + endpoint + '.json'
        with patch('os.path.join', return_value=expected_filename):
            result = task_func(api_url, endpoint, prefix)
        self.assertEqual(result, expected_filename)

    @patch('requests.get')
    def test_successful_data_fetch_different_filename(self, mock_get):
        mock_data = {'name': 'test', 'value': 123}
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_data)
        api_url = 'https://fakeapi.com/'
        endpoint = 'temp'
        prefix = 'PREFIX_'
        expected_filename = prefix + endpoint + '.json'
        with patch('os.path.join', return_value=expected_filename):
            result = task_func(api_url, endpoint, prefix)
        self.assertEqual(result, expected_filename)
