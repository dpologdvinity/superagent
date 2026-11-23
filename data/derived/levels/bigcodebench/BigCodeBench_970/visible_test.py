from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

class TestCases(unittest.TestCase):

    def tearDown(self):
        plt.close('all')

    def helper_assert_plot_attributes(self, ax):
        self.assertIsInstance(ax, plt.Axes)
        self.assertIn('Cumulative Probability Plot', ax.get_title())
        self.assertIn('Index', ax.get_xlabel())
        self.assertIn('Cumulative Probability', ax.get_ylabel())
        lines = ax.get_lines()
        self.assertIsInstance(lines[0], Line2D, 'The plot should contain a Line2D object.')
        self.assertEqual(lines[0].get_marker(), 'o', "The marker should be 'o'.")
        self.assertEqual(lines[0].get_linestyle(), '-', "The linestyle should be '-'.")

    def helper_assert_cumulative_probability_correctness(self, ax, expected_cumulative_prob):
        line = ax.get_lines()[0]
        np.testing.assert_array_almost_equal(line.get_ydata(), expected_cumulative_prob, decimal=2, err_msg='Cumulative probability calculation is incorrect.')

    def test_negative_numbers(self):
        data = np.array([-1, 0, 1, 2, 3])
        with self.assertRaises(ValueError):
            task_func(data)

    def test_nan_values(self):
        data = np.array([1, 2, 3, np.nan, 5])
        with self.assertRaises(ValueError):
            task_func(data)

    def test_non_numeric_values(self):
        data = np.array([1, 2, 3, 'hello', 5])
        with self.assertRaises(TypeError):
            task_func(data)
