from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json

class TestCases(unittest.TestCase):

    def test_normal_json_input(self):
        """Test with normal JSON input with various punctuation."""
        json_input = '{"text": "Hello world! Hello universe. World, meet universe."}'
        expected_output = {'hello': 2, 'world': 2, 'universe': 2, 'meet': 1}
        self.assertEqual(task_func(json_input), expected_output)

    def test_missing_text_field(self):
        """Test with JSON input with no 'text' field."""
        json_input = '{"data": "Some data without text field."}'
        expected_output = {}
        self.assertEqual(task_func(json_input), expected_output)

    def test_numbers_and_special_characters(self):
        """Test with JSON input containing numbers and special characters."""
        json_input = '{"text": "12345 test! Special #characters and numbers 67890."}'
        expected_output = {'12345': 1, 'test': 1, 'special': 1, 'characters': 1, 'and': 1, 'numbers': 1, '67890': 1}
        self.assertEqual(task_func(json_input), expected_output)
