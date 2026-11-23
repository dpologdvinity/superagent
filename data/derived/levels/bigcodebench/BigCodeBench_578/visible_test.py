from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, Mock
import requests

class TestCases(unittest.TestCase):

    @patch('requests.get')
    def test_return_type(self, mock_get):
        mock_get.return_value.json.return_value = {'login': 'user', 'name': 'Test User'}
        result = task_func('user')
        self.assertIsInstance(result, dict)

    @patch('requests.get')
    def test_normalized_string(self, mock_get):
        mock_get.return_value.json.return_value = {'login': 'user', 'name': 'Tést Üser'}
        result = task_func('user')
        self.assertEqual(result['name'], 'Test User')

    @patch('requests.get')
    def test_non_string_values(self, mock_get):
        mock_get.return_value.json.return_value = {'login': 'user', 'id': 12345}
        result = task_func('user')
        self.assertEqual(result['id'], 12345)
