from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import unittest

class TestCases(unittest.TestCase):
    """Test cases for the function task_func."""

    def test_default_dataset(self):
        """Test the function with default dataset."""
        result = task_func()
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (100, 5))

    def test_small_dataset(self):
        """Test the function with a small dataset."""
        data = np.array([[0.1, 0.9], [0.4, 0.8]])
        result = task_func(data)
        self.assertEqual(result.shape, (2, 2))

    def test_replacement(self):
        """Test the replacement of values less than 0.5."""
        data = np.array([[0.1, 0.9], [0.4, 0.8]])
        result = task_func(data)
        self.assertNotIn(0.1, result.values)
        self.assertNotIn(0.4, result.values)
