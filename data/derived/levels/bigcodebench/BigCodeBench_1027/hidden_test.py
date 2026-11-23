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
        url = "https://www.example.com?q=4a4b4c"
        self.assertEqual(task_func(url), "JKL")
    def test_no_query_parameter(self):
        """Test with no query parameter."""
        url = "https://www.example.com"
        self.assertIsNone(task_func(url))
    def test_invalid_hex_string(self):
        """Test with an invalid hex string in query parameter."""
        url = "https://www.example.com?q=4a4b4c4d4"
        self.assertIsNone(
            task_func(url)
        )  # Updated to assertIsNone as the function now handles the exception
    def test_valid_hex_non_utf8(self):
        """Test with a valid hex string that is not valid UTF-8."""
        url = "https://www.example.com?q=80"
        self.assertIsNone(
            task_func(url)
        )  # Updated to assertIsNone due to the handling of UnicodeDecodeError
    def test_multiple_query_parameters(self):
        """Test with multiple query parameters."""
        url = "https://www.example.com?a=123&q=4a4b4c&b=456"
        self.assertEqual(task_func(url), "JKL")
