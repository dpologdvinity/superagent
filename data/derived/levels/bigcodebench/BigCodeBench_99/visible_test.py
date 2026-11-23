from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def setUp(self):
        self.fig = task_func()

    def test_figure_type(self):
        self.assertIsInstance(self.fig, plt.Figure, 'The returned object should be a matplotlib Figure.')

    def test_axes_existence(self):
        self.assertGreater(len(self.fig.axes), 0, 'The figure should contain one or more axes.')

    def test_figure_children(self):
        self.assertGreater(len(self.fig.get_children()), 0, 'The figure should have children.')
