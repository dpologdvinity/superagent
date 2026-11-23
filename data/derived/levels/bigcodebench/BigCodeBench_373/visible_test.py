from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np

class TestCases(unittest.TestCase):

    def test_case_1(self):
        l = np.array([1, 4, 9, 16, 25])
        x_data = np.array([1, 2, 3, 4, 5])
        params, fitted_values = task_func(l, x_data)
        self.assertAlmostEqual(params[0], 1.0, places=5)
        self.assertAlmostEqual(params[1], 0, places=5)
        np.testing.assert_array_almost_equal(fitted_values, l, decimal=5)

    def test_case_2(self):
        l = np.array([2, 5, 10, 17, 26])
        x_data = np.array([1, 2, 3, 4, 5])
        params, fitted_values = task_func(l, x_data)
        np.testing.assert_array_almost_equal(fitted_values, l, decimal=5)

    def test_case_3(self):
        l = np.array([0, 3, 8, 15, 24])
        x_data = np.array([1, 2, 3, 4, 5])
        params, fitted_values, ax = task_func(l, x_data, plot=True)
        np.testing.assert_array_almost_equal(fitted_values, l, decimal=5)
        self.assertIsInstance(ax, plt.Axes)
