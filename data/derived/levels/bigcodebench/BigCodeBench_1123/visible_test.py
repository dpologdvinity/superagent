from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock
import unittest
import re
import urllib.parse
import ssl
import socket

class TestCases(unittest.TestCase):

    def setUp(self):
        self.patcher1 = patch('socket.create_connection')
        self.patcher2 = patch('ssl.create_default_context')
        self.mock_create_connection = self.patcher1.start()
        self.mock_create_default_context = self.patcher2.start()
        self.mock_socket = MagicMock()
        self.mock_ssl_context = MagicMock()
        self.mock_ssl_socket = MagicMock()
        self.mock_create_connection.return_value.__enter__.return_value = self.mock_socket
        self.mock_create_default_context.return_value = self.mock_ssl_context
        self.mock_ssl_context.wrap_socket.return_value.__enter__.return_value = self.mock_ssl_socket

    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()

    def test_basic_https_functionality(self):
        """Test extracting SSL expiry from properly formatted HTTPS URLs."""
        self.mock_ssl_socket.getpeercert.return_value = {'notAfter': '2023-06-15 12:00:00'}
        input_str = 'https://www.google.com, https://www.python.org'
        result = task_func(input_str)
        expected = {'www.google.com': '2023-06-15 12:00:00', 'www.python.org': '2023-06-15 12:00:00'}
        self.assertEqual(result, expected)

    def test_urls_with_ports_and_queries(self):
        """Test HTTPS URLs that include port numbers and query strings."""
        self.mock_ssl_socket.getpeercert.return_value = {'notAfter': '2023-06-15 12:00:00'}
        input_str = 'https://www.example.com:8080/page?query=test, https://api.example.org/data?info=value'
        result = task_func(input_str)
        expected = {'www.example.com:8080': '2023-06-15 12:00:00', 'api.example.org': '2023-06-15 12:00:00'}
        self.assertEqual(result, expected)

    def test_no_urls(self):
        """Test input with no URLs resulting in an empty dictionary."""
        result = task_func('No links here!')
        self.assertEqual(result, {})
