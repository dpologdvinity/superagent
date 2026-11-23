from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(ValueError):
            ax = task_func(0, 1, 0, 77)

    def test_case_2(self):
        mu, sigma, sample_size, seed = (0, 1, 10000, 42)
        ax = task_func(mu, sigma, sample_size, seed)
        line = ax.lines[0]
        x_data, y_data = line.get_data()
        assert isinstance(ax, matplotlib.axes._axes.Axes)
        assert min(x_data) < mu - 3 * sigma and max(x_data) > mu + 3 * sigma

    def test_case_3(self):
        ax = task_func(0, 1, 10000, 42)
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        assert xlim[0] < 0 and xlim[1] > 0
        assert ylim[0] < 0 and ylim[1] > 0
