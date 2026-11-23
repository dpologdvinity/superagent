from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import re
import os
from unittest.mock import mock_open, patch

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    def setUp(self):
        """Set up the environment for testing by creating test files."""
        with open('test.txt', 'w', encoding='utf-8') as f:
            f.write('This is a test file.')

    def tearDown(self):
        """Clean up the environment by deleting the test files created."""
        os.remove('test.txt')

    def test_file_found(self):
        """Test the response when the requested file is found."""
        request = 'GET /test.txt HTTP/1.1'
        expected_response = 'HTTP/1.1 200 OK\r\nContent-Length: 20\r\n\r\nThis is a test file.'
        self.assertEqual(task_func(request), expected_response)

    def test_file_not_found(self):
        """Test the response when the requested file is not found."""
        request = 'GET /nonexistent.txt HTTP/1.1'
        expected_response = 'HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found'
        self.assertEqual(task_func(request), expected_response)

    def test_bad_request(self):
        """Test the response for a badly formatted request."""
        request = 'BAD REQUEST'
        expected_response = 'HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request'
        self.assertEqual(task_func(request), expected_response)
