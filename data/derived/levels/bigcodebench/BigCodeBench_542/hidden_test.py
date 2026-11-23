from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_normal_functionality(self):
        """Test the function with default parameters."""
        result = task_func()
        self.assertIsInstance(result, str)
    def test_custom_keys_list(self):
        """Test the function with a custom list of hexadecimal keys."""
        custom_keys = ['1A2FC614', '1B0FC614', '1C9FC614']
        result = task_func(hex_keys=custom_keys)
        self.assertIsInstance(result, str)
    def test_empty_key_list(self):
        """Test the function with an empty list to check for error handling."""
        with self.assertRaises(IndexError):
            task_func(hex_keys=[])
    def test_invalid_hexadecimal(self):
        """Test the function with an invalid hexadecimal string."""
        invalid_keys = ['ZZZ', '4A0FC614']
        with self.assertRaises(ValueError):
            task_func(hex_keys=invalid_keys)
    def test_consistent_output_with_same_seed(self):
        """Test that the same seed returns the same result."""
        result1 = task_func(seed=99)
        result2 = task_func(seed=99)
        self.assertEqual(result1, result2)
