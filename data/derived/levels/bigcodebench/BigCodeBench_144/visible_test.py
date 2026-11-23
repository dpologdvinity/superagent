from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock
import requests

class TestCases(unittest.TestCase):

    @patch('requests.get')
    def test_return_type(self, mock_get):
        """Test that the function returns a list."""
        mock_get.side_effect = requests.exceptions.ConnectionError
        result = task_func('192.168.0.0/30', 5)
        self.assertIsInstance(result, list)

    @patch('requests.get')
    def test_handle_exceptions(self, mock_get):
        """Test that the function handles exceptions properly by not including IPs with failed requests."""
        mock_get.side_effect = [requests.exceptions.ConnectionError] * 4
        result = task_func('192.168.0.0/30', 5)
        expected_result = []
        self.assertEqual(result, expected_result, 'task_func should skip IPs that failed to connect.')

    @patch('requests.get')
    def test_active_server(self, mock_get):
        """
        Test that the function correctly identifies and includes active servers in the IP range.
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        ip_range = '192.168.1.0/30'
        result = task_func(ip_range, 5)
        expected_result = ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3']
        self.assertEqual(result, expected_result, 'The function should identify and include all active servers in the range.')
