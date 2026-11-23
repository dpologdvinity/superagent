from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import binascii
import urllib.parse

class TestCases(unittest.TestCase):
    """Test cases for task_func."""

    def test_valid_hex_string(self):
        """Test with a valid hex string in query parameter."""
        url = 'https://www.example.com?q=4a4b4c'
        self.assertEqual(task_func(url), 'JKL')

    def test_no_query_parameter(self):
        """Test with no query parameter."""
        url = 'https://www.example.com'
        self.assertIsNone(task_func(url))

    def test_invalid_hex_string(self):
        """Test with an invalid hex string in query parameter."""
        url = 'https://www.example.com?q=4a4b4c4d4'
        self.assertIsNone(task_func(url))
