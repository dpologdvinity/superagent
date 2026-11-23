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
        json_filename = 'updated_dictionary.json'
        txt_filename = 'key_frequencies.txt'
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
