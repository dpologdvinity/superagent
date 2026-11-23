from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_standard_input(self):
        """Test with standard input containing words, punctuation, and whitespaces"""
        input_text = 'Hello, world! This is a test.'
        expected_output = ['hello', 'world', 'this', 'is', 'a', 'test']
        self.assertEqual(task_func(input_text), expected_output)

    def test_empty_string(self):
        """Test with an empty string"""
        input_text = ''
        expected_output = ['']
        self.assertEqual(task_func(input_text), expected_output)

    def test_string_with_no_punctuation(self):
        """Test with a string that has no punctuation marks"""
        input_text = 'Python is great'
        expected_output = ['python', 'is', 'great']
        self.assertEqual(task_func(input_text), expected_output)
