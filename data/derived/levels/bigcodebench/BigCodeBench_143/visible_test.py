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
        solution_point = ax.lines[-1]
        self.assertTrue(solution_point.get_marker() == 'o')
        color = solution_point.get_color()
        expected_green = matplotlib.colors.to_rgba('g')
        actual_color_rgba = matplotlib.colors.to_rgba(color)
        self.assertTrue(np.allclose(actual_color_rgba, expected_green, atol=0.01), f'Actual color {actual_color_rgba} not close to expected green {expected_green}')
