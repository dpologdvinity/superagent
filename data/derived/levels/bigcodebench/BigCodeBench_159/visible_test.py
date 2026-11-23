from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np

class TestCases(unittest.TestCase):

    def test_return_type(self):
        """Test that the function returns bytes."""
        result = task_func(np.array([1, 2, 3]))
        self.assertIsInstance(result, bytes)

    def test_gzipped_data_size(self):
        """Test the size of the gzipped data is greater than 0."""
        data = task_func(np.array([1, 2, 3]))
        self.assertGreater(len(data), 0)

    def test_with_different_array_sizes(self):
        """Ensure larger arrays produce gzipped data of greater or equal size compared to smaller arrays."""
        small_array = task_func(np.array([1]))
        larger_array = task_func(np.array(range(100)))
        self.assertGreaterEqual(len(larger_array), len(small_array))
