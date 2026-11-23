from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np
from matplotlib.axes import Axes

class TestCases(unittest.TestCase):
    """Test cases for the function task_func."""

    def test_with_random_data(self):
        """
        Test the function with random data to ensure normal functionality.
        """
        np.random.seed(42)
        feature = pd.Series(np.random.rand(100))
        np.random.seed(42)
        target = pd.Series(np.random.randint(0, 2, size=100))
        cm, ax = task_func(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)

    def test_with_all_zeroes(self):
        """
        Test the function with all zeroes in the feature set.
        """
        feature = pd.Series(np.zeros(100))
        np.random.seed(123)
        target = pd.Series(np.random.randint(0, 2, size=100))
        cm, ax = task_func(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)

    def test_with_all_ones(self):
        """
        Test the function with all ones in the feature set.
        """
        feature = pd.Series(np.ones(100))
        np.random.seed(42)
        target = pd.Series(np.random.randint(0, 2, size=100))
        cm, ax = task_func(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)

    def tearDown(self):
        plt.close()
