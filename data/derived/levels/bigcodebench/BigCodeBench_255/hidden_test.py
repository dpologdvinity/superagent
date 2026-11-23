from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, polar=True)
    def test_sine_function(self):
        ax = task_func(self.ax, 0)
        self.assertIsNotNone(ax, "Ax should not be None")
        # Verify if the plotted function matches the sine function
        x = np.linspace(0, 2 * np.pi, 1000)
        y_expected = np.sin(x)
        y_actual = ax.lines[0].get_ydata()
        np.testing.assert_allclose(y_actual, y_expected, atol=1e-5)
    def test_cosine_function(self):
        ax = task_func(self.ax, 1)
        self.assertIsNotNone(ax, "Ax should not be None")
    def test_tangent_function(self):
        ax = task_func(self.ax, 2)
        self.assertIsNotNone(ax, "Ax should not be None")
    def test_invalid_index(self):
        with self.assertRaises(IndexError):
            task_func(self.ax, 3)
    def test_rlabel_position(self):
        ax = task_func(self.ax, 1)
        self.assertEqual(ax.get_rlabel_position(), 45, "Rlabel position should be 45 for index 1")
    def test_case_non_ax(self):
        with self.assertRaises(ValueError):
            task_func("non_ax", 1)
