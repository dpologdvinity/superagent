from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch

class TestCases(unittest.TestCase):

    def setUp(self):
        self.salt_size = 16

    def test_return_type(self):
        """Test that the function returns a tuple."""
        result = task_func('F3BE8080', self.salt_size)
        self.assertIsInstance(result, tuple)

    def test_salt_and_hash_length(self):
        """Test the length of the salt and hash."""
        salt, hash_value = task_func('F3BE8080', self.salt_size)
        self.assertEqual(len(salt), 24)
        self.assertEqual(len(hash_value), 64)

    def test_hash_changes_with_input(self):
        """Test that different inputs produce different hashes."""
        _, hash1 = task_func('F3BE8080', self.salt_size)
        _, hash2 = task_func('F4BE8080', self.salt_size)
        self.assertNotEqual(hash1, hash2)
