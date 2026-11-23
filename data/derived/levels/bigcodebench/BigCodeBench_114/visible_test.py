from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
from unittest.mock import patch

class TestCases(unittest.TestCase):

    def test_return_type(self):
        """Test that the function returns a dictionary."""
        result = task_func({'array': np.array([1, 2, 3])})
        self.assertIsInstance(result, dict)

    def test_normalized_array_presence(self):
        """Test that 'normalized_array' key is present in the returned dictionary."""
        result = task_func({'array': np.array([1, 2, 3])})
        self.assertIn('normalized_array', result)

    def test_normalized_array_values(self):
        """Test that the normalized array contains correct values."""
        input_array = np.array([10, 20, 30])
        expected_normalized = np.array([0.0, 0.5, 1.0])
        result = task_func({'array': input_array})
        np.testing.assert_array_almost_equal(result['normalized_array'], expected_normalized)
