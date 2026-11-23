from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    """Test cases for the function task_func."""

    def test_basic_functionality(self):
        """Test the basic functionality of the function."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        ax = task_func(arr)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Time Series of Row Sums')
        y_data = [line.get_ydata() for line in ax.get_lines()][0]
        expected_sums = arr.sum(axis=1)
        np.testing.assert_array_equal(y_data, expected_sums)

    def test_empty_array(self):
        """Test the function with an empty array."""
        arr = np.array([])
        ax = task_func(arr)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Time Series of Row Sums')
        lines = ax.get_lines()
        self.assertEqual(len(lines), 0)

    def test_single_row_array(self):
        """Test the function with a single row array."""
        arr = np.array([[1, 2, 3]])
        ax = task_func(arr)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Time Series of Row Sums')
        y_data = [line.get_ydata() for line in ax.get_lines()][0]
        expected_sum = arr.sum(axis=1)
        np.testing.assert_array_equal(y_data, expected_sum)

    def tearDown(self):
        plt.close()
