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
    def test_phase_calculation(self):
        """Test phase calculation for known values."""
        x = np.array([1, -1])
        y = np.array([0, 0])
        _, Z = task_func(x, y)
        expected_phases = np.array([cmath.phase((1 + 0j)**2 - 1), cmath.phase((-1 + 0j)**2 - 1)])
        np.testing.assert_array_almost_equal(Z[0], expected_phases)
    def test_mismatched_array_sizes(self):
        """Test function with arrays of different lengths."""
        with self.assertRaises(ValueError):
            task_func(np.array([0]), np.array([0, 1]))
