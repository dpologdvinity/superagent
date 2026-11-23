from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, Mock
class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_case_1(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response
        
        # Test
        result = task_func('Fetch data from https://api.example.com/data')
        self.assertEqual(result, {"key": "value"})
    @patch('requests.get')
    def test_case_2(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"data": [1, 2, 3]}
        mock_get.return_value = mock_response
        
        # Test
        result = task_func('Get numbers from https://api.example.com/numbers')
        self.assertEqual(result, {"data": [1, 2, 3]})
    @patch('requests.get')
    def test_case_3(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response
        
        # Test
        result = task_func('Fetch empty data from https://api.example.com/empty')
        self.assertEqual(result, {})
    @patch('requests.get')
    def test_case_4(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"status": "OK"}
        mock_get.return_value = mock_response
        
        # Test
        result = task_func('Check status from https://api.example.com/status')
        self.assertEqual(result, {"status": "OK"})
    @patch('requests.get')
    def test_case_5(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"users": ["Alice", "Bob", "Charlie"]}
        mock_get.return_value = mock_response
        
        # Test
        result = task_func('List users from https://api.example.com/users')
        self.assertEqual(result, {"users": ["Alice", "Bob", "Charlie"]})
