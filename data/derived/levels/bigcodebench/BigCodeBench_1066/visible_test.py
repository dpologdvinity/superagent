from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    """Test cases for the function task_func."""

    def test_default_values(self):
        """Test the function with default values."""
        np.random.seed(0)
        data, _, _ = task_func()
        self.assertEqual(len(data), 105)

    def test_custom_values(self):
        """Test the function with custom values."""
        np.random.seed(1)
        data, outliers_detected, _ = task_func(num_samples=50, num_outliers=10)
        self.assertEqual(len(data), 60)
        normal_data = data[:50]
        q75, q25 = np.percentile(normal_data, [75, 25])
        iqr = q75 - q25
        lower_bound = q25 - iqr * 1.5
        upper_bound = q75 + iqr * 1.5
        expected_outliers_count = len([o for o in data if o < lower_bound or o > upper_bound])
        self.assertEqual(len(outliers_detected), expected_outliers_count)

    def test_no_outliers(self):
        """Test the function with no outliers."""
        np.random.seed(2)
        data, outliers_detected, ax = task_func(num_samples=100, num_outliers=0)
        self.assertEqual(len(data), 100)
        self.assertTrue(len(outliers_detected) <= 1)

    def tearDown(self):
        plt.close()
