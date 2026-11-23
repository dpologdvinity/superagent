from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    """Tests for `task_func`."""
    def test_histogram_and_pdf(self):
        """Test that the histogram and PDF are plotted."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        ax, _ = task_func(arr)
        self.assertEqual(
            ax.get_title(),
            "Histogram of Normalized Data with Standard Normal PDF",
        )
        self.assertEqual(len(ax.lines), 1)
        self.assertEqual(len(ax.patches), 30)
    def test_normalized_data(self):
        """Test that the normalized data is correct."""
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        _, normalized_data = task_func(arr)
        expected_data = [-1.22474487, 0.0, 1.22474487]
        for i in range(len(expected_data)):
            self.assertTrue(np.isclose(normalized_data[i], expected_data[i]))
    def test_empty_array(self):
        """Test empty array."""
        arr = np.array([[], [], []])
        _, normalized_data = task_func(arr)
        for value in normalized_data:
            self.assertTrue(np.isclose(value, 0))
    def test_single_value_array(self):
        """Test single value array."""
        arr = np.array([[5], [5], [5]])
        _, normalized_data = task_func(arr)
        for value in normalized_data:
            self.assertTrue(np.isclose(value, 0))
    def test_large_values(self):
        """Test large values."""
        arr = np.array([[1e6, 2e6, 3e6], [4e6, 5e6, 6e6], [7e6, 8e6, 9e6]])
        _, normalized_data = task_func(arr)
        expected_data = [-1.22474487, 0.0, 1.22474487]
        for i in range(len(expected_data)):
            self.assertTrue(np.isclose(normalized_data[i], expected_data[i]))
