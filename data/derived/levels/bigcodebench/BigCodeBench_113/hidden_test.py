from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    def tearDown(self):
        json_filename = "updated_dictionary.json"
        txt_filename = "key_frequencies.txt"
        if os.path.exists(json_filename):
            os.remove(json_filename)
        if os.path.exists(txt_filename):
            os.remove(txt_filename)
        
    def test_return_type(self):
        """Test that the function returns the correct tuple types."""
        result, json_path, txt_path = task_func({}, self.keys)
        self.assertIsInstance(result, dict)
        self.assertIsInstance(json_path, str)
        self.assertIsInstance(txt_path, str)
    def test_new_keys_added(self):
        """Test that new keys are added to the dictionary."""
        result, _, _ = task_func({}, self.keys)
        for key in self.keys:
            self.assertIn(key, result)
    def test_original_keys_preserved(self):
        """Test that original keys in the dictionary are preserved."""
        original_dict = {'x': 200, 'y': 300}
        result, _, _ = task_func(original_dict.copy(), self.keys)
        self.assertIn('x', result)
        self.assertIn('y', result)
    def test_values_within_range(self):
        """Test that all values are within the specified range 1-100."""
        result, _, _ = task_func({}, self.keys)
        for value in result.values():
            self.assertTrue(1 <= value <= 100)
    def test_dictionary_length_update(self):
        """Test that the dictionary length is correctly updated."""
        original_dict = {'x': 200, 'y': 300}
        expected_length = len(original_dict) + len(self.keys)
        result, _, _ = task_func(original_dict.copy(), self.keys)
        self.assertEqual(len(result), expected_length)
    def test_files_created(self):
        """Test that JSON and TXT files are created."""
        _, json_path, txt_path = task_func({}, self.keys)
        self.assertTrue(os.path.exists(json_path))
        self.assertTrue(os.path.exists(txt_path))
    def test_value_error_raised_for_invalid_keys(self):
        """Test that a ValueError is raised if 'keys' does not contain exactly 10 unique elements."""
        with self.assertRaises(ValueError):
            task_func({}, ['a', 'b'])  # Not enough keys
    @patch('random.randint', return_value=50)
    def test_mock_random(self, mock_randint):
        """Test the function with a mock of the random.randint function."""
        result, _, _ = task_func({}, self.keys)
        mock_randint.assert_called()
        for key in self.keys:
            self.assertEqual(result[key], 50)
