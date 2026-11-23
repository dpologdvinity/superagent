from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for task_func."""
    def test_default_parameters(self):
        """
        Test task_func with default parameters.
        """
        np.random.seed(0)
        skewness, kurtosis, plot_paths = task_func()
        self.assertAlmostEqual(skewness, 0, delta=0.5)
        self.assertAlmostEqual(kurtosis, 0, delta=0.5)
        self.assertEqual(len(plot_paths), 0)
    def test_save_plots_true(self):
        """
        Test task_func with save_plots set to True.
        """
        np.random.seed(1)
        _, _, plot_paths = task_func(save_plots=True)
        self.assertEqual(len(plot_paths), 2)
        for path in plot_paths:
            self.assertTrue(os.path.exists(path))
            os.remove(path)  # Clean up: remove created files
    def test_custom_mean_std_dev(self):
        """
        Test task_func with custom mean and standard deviation.
        """
        np.random.seed(2)
        mean = 100
        std_dev = 10
        skewness, kurtosis, _ = task_func(mean, std_dev)
        self.assertAlmostEqual(skewness, 0, delta=1)
        self.assertAlmostEqual(kurtosis, 0, delta=1)
    def test_negative_std_dev(self):
        """
        Test task_func with a negative standard deviation.
        """
        np.random.seed(3)
        with self.assertRaises(ValueError):
            task_func(std_dev=-1)
    def test_large_sample(self):
        """
        Test task_func with a larger sample size.
        """
        np.random.seed(4)
        _, _, plot_paths = task_func(mean=1000, std_dev=50, save_plots=True)
        self.assertEqual(len(plot_paths), 2)
        for path in plot_paths:
            self.assertTrue(os.path.exists(path))
            os.remove(path)  # Clean up: remove created files
