from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
import matplotlib
class TestCases(unittest.TestCase):
    def test_return_type(self):
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)
    def test_line_plot(self):
        ax = task_func()
        line = ax.lines[0]
        self.assertEqual(line.get_label(), 'y=2x+1')
    def test_solution_plot(self):
        ax = task_func()
        # Find the solution point among line plots
        # Assuming the last added line plot is the solution point
        solution_point = ax.lines[-1]  # Get the last line plot, which should be the solution
        self.assertTrue(solution_point.get_marker() == 'o')  # Check marker shape
        color = solution_point.get_color()
        expected_green = matplotlib.colors.to_rgba('g')
        # We convert both the actual color and the expected 'green' color to RGBA format for a proper comparison
        actual_color_rgba = matplotlib.colors.to_rgba(color)
        self.assertTrue(np.allclose(actual_color_rgba, expected_green, atol=0.01), f"Actual color {actual_color_rgba} not close to expected green {expected_green}")
    def test_plot_title_and_labels(self):
        ax = task_func()
        self.assertEqual(ax.get_title(), 'Solution of the equation y=2x+1 at x=2')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
    def test_solution_accuracy(self):
        ax = task_func()
        solution_point = ax.lines[-1]  # Get the last line plot, which should be the solution
        x_data, y_data = solution_point.get_data()
        self.assertAlmostEqual(x_data[0], 2)  # x coordinate of the solution
        self.assertAlmostEqual(y_data[0], 5)  # y coordinate of the solution
    def test_x_range(self):
        ax = task_func()
        self.assertEqual(ax.get_xlim(), (-10, 10))  # Check if the x-axis range is set as expected
