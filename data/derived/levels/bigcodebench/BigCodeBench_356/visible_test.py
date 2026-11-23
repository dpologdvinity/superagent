from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
import cmath

class TestCases(unittest.TestCase):

    def test_input_types(self):
        """Test the function with non-numpy array inputs."""
        with self.assertRaises(TypeError):
            task_func([1, 2, 3], np.array([1, 2, 3]))

    def test_empty_arrays(self):
        """Test function with empty numpy arrays."""
        _, Z = task_func(np.array([]), np.array([]))
        self.assertEqual(Z.size, 0)

    def test_single_point(self):
        """Test the function with single-point arrays."""
        ax, Z = task_func(np.array([0]), np.array([0]))
        self.assertIsInstance(ax, plt.Axes)
        self.assertIsInstance(Z, np.ndarray)
