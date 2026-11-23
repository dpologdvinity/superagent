from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import json
from faker import Faker
fake = Faker()

class TestCases(unittest.TestCase):

    def setUp(self):
        """Create the test file with initial data."""
        self.filename = 'data.json'
        self.data = {'key': 'value'}
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def tearDown(self):
        """Remove the test file after all tests."""
        os.remove(self.filename)

    def test_empty_dict(self):
        """Test with an empty dictionary to ensure it writes and verifies correctly."""
        filename = 'empty_test.json'
        data = {}
        success, content = task_func(filename, data)
        self.assertTrue(success)
        self.assertEqual(content, data)
        os.remove(filename)

    def test_simple_dict(self):
        """Test with a simple dictionary to check for basic write and verify functionality."""
        filename = 'simple_test.json'
        data = {'key': 'value'}
        success, content = task_func(filename, data)
        self.assertTrue(success)
        self.assertEqual(content, data)
        os.remove(filename)

    def test_nested_dict(self):
        """Test with a nested dictionary to ensure nested structures are handled correctly."""
        filename = 'nested_test.json'
        data = {'key': {'nested_key': 'nested_value'}}
        success, content = task_func(filename, data)
        self.assertTrue(success)
        self.assertEqual(content, data)
        os.remove(filename)
