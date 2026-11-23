from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import binascii
import hashlib

class TestCases(unittest.TestCase):
    """Tests for task_func."""

    def test_string_with_numbers(self):
        """Test that the function returns the correct hash for a string with numbers."""
        self.assertEqual(task_func('4a4b4c'), '1a3db6ced8854274567d707b509f7486a9244be0cab89217713fce9bf09f522e')

    def test_string_with_space(self):
        """Test that the function returns the correct hash for a string with space."""
        self.assertEqual(task_func('Open AI'), 'dd7503942d7be003d6faaa93d9951126fde3bdd4f3484404927e79585682878a')

    def test_empty_string(self):
        """Test that the function returns the correct hash for an empty string."""
        self.assertEqual(task_func(''), 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')
