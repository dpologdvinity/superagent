from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import numpy as np
import unittest
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_uniform_distribution(self):
        """Test uniform distribution."""
        arr = np.array(["A", "A", "B", "B"])
        uniform, _ = task_func(arr)
        self.assertTrue(uniform)
    def test_non_uniform_distribution(self):
        """Test non-uniform distribution."""
        arr = np.array(["A", "A", "B", "B", "B", "C", "C", "C", "C", "D", "E", "E"])
        uniform, _ = task_func(arr)
        self.assertFalse(uniform)
    def test_single_value(self):
        """Test single value."""
        arr = np.array(["A", "A", "A", "A"])
        uniform, _ = task_func(arr)
        self.assertTrue(uniform)
    def test_multiple_equal_values(self):
        """Test multiple equal values."""
        arr = np.array(["A", "A", "B", "B", "C", "C", "D", "D"])
        uniform, _ = task_func(arr)
        self.assertTrue(uniform)
    def test_varying_values(self):
        """Test varying values."""
        arr = np.array(["A", "B", "B", "C", "C", "C", "D", "D", "D", "D"])
        uniform, _ = task_func(arr)
        self.assertFalse(uniform)
    def tearDown(self):
        plt.close()
