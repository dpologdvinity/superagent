from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a single valid URL
        input_str = "Visit http://www.google.com for more details."
        with patch('socket.gethostbyname', return_value='192.0.2.1'):
            result = task_func(input_str)
            self.assertEqual(result, {'www.google.com': '192.0.2.1'})
    def test_case_2(self):
        # Test with multiple valid URLs
        input_str = "Check these links: http://www.google.com, https://www.python.org"
        with patch('socket.gethostbyname', side_effect=['192.0.2.1', '192.0.2.2']):
            result = task_func(input_str)
            self.assertEqual(result, {'www.google.com': '192.0.2.1', 'www.python.org': '192.0.2.2'})
    def test_case_3(self):
        # Test with a string that doesn't contain any URLs
        input_str = "Hello, World!"
        result = task_func(input_str)
        self.assertEqual(result, {})
    def test_case_4(self):
        # Test with a string containing invalid URLs
        input_str = "Check these: randomtext, another:randomtext"
        result = task_func(input_str)
        self.assertEqual(result, {})
    def test_case_5(self):
        # Test with a string containing valid and invalid URLs
        input_str = "Valid: http://www.google.com, Invalid: randomtext"
        with patch('socket.gethostbyname', return_value='192.0.2.1'):
            result = task_func(input_str)
            self.assertEqual(result, {'www.google.com': '192.0.2.1'})
    def test_case_6(self):
        # Test with a domain that cannot be resolved
        input_str = "Visit http://nonexistent.domain.com"
        with patch('socket.gethostbyname', side_effect=socket.gaierror):
            result = task_func(input_str)
            self.assertEqual(result, {'nonexistent.domain.com': None})
