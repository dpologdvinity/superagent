from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import http.client
import ssl
import socket

class TestCases(unittest.TestCase):

    @patch('http.client.HTTPSConnection')
    def test_return_type(self, mock_conn):
        """ Test that the function returns a string. """
        mock_conn.return_value.getresponse.return_value.read.return_value = b'Server Response'
        result = task_func('www.example.com', 443, '/test/path')
        self.assertIsInstance(result, str)

    @patch('http.client.HTTPSConnection')
    def test_different_paths(self, mock_conn):
        """ Test the function with different request paths. """
        mock_conn.return_value.getresponse.return_value.read.return_value = b'Server Response'
        result = task_func('www.example.com', 443, '/another/path')
        self.assertIsInstance(result, str)

    @patch('http.client.HTTPSConnection')
    def test_connection_error_handling(self, mock_conn):
        """ Test handling of connection errors. """
        mock_conn.side_effect = http.client.HTTPException('Connection error')
        with self.assertRaises(http.client.HTTPException):
            task_func('www.example.com', 443, '/error/path')
