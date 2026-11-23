from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        ax = task_func(0, 1)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.collections) > 0, 'The plot should have data.')
        self.assertTrue(ax.get_figure().colorbar is not None)

    def test_case_2(self):
        ax = task_func(2, 0.5)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.collections) > 0, 'The plot should have data.')
        self.assertTrue(len(ax.collections[0].get_offsets()) > 0)

    def test_case_3(self):
        ax = task_func(-2, 2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.collections) > 0, 'The plot should have data.')
