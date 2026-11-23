from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json
class TestCases(unittest.TestCase):
    def test_normal_json_input(self):
        """Test with normal JSON input with various punctuation."""
        # Description: This test ensures that the function can accurately count words
        # in a JSON string that contains typical sentence punctuation.
        json_input = '{"text": "Hello world! Hello universe. World, meet universe."}'
        expected_output = {'hello': 2, 'world': 2, 'universe': 2, 'meet': 1}
        self.assertEqual(task_func(json_input), expected_output)
    def test_missing_text_field(self):
        """Test with JSON input with no 'text' field."""
        # Description: This test checks the function's behavior when the JSON string
        # does not have a "text" field, expecting an empty dictionary in return.
        json_input = '{"data": "Some data without text field."}'
        expected_output = {}
        self.assertEqual(task_func(json_input), expected_output)
    def test_numbers_and_special_characters(self):
        """Test with JSON input containing numbers and special characters."""
        # Description: This test verifies that numbers and special characters are not counted
        # as words and that they are properly removed before word counting.
        json_input = '{"text": "12345 test! Special #characters and numbers 67890."}'
        expected_output = {'12345': 1, 'test': 1, 'special': 1, 'characters': 1, 'and': 1, 'numbers': 1, '67890': 1}
        self.assertEqual(task_func(json_input), expected_output)
    def test_large_text_input(self):
        """Test with a large text input to check performance and accuracy."""
        # Description: This test uses a large block of text to assess the function's
        # performance and accuracy in processing and counting words.
        json_input = '{"text": "' + " ".join(["word"] * 1000) + '"}'
        expected_output = {'word': 1000}
        self.assertEqual(task_func(json_input), expected_output)
    def test_malformed_json_input(self):
        """Test with a malformed JSON input."""
        # Description: This test checks the function's ability to handle a JSON string that
        # is not properly formatted. The function is expected to return an empty dictionary.
        json_input = '{"text: "This is not a properly formatted JSON string."}'
        expected_output = {}
        self.assertEqual(task_func(json_input), expected_output)
