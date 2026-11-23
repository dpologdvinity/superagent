from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
from matplotlib.container import BarContainer
import random

class TestCases(unittest.TestCase):
    """Tests for the function task_func."""

    def test_return_type(self):
        """Verify the returned type of the function."""
        random.seed(0)
        ax = task_func(5)
        self.assertIsInstance(ax, BarContainer, 'The returned object is not of the expected type.')

    def test_number_of_bars(self):
        """Verify the number of bars plotted for different `n_pairs` values."""
        random.seed(1)
        for i in [5, 10, 20]:
            ax = task_func(i)
            self.assertEqual(len(ax.patches), i, f'Expected {i} bars, but got {len(ax.patches)} bars.')

    def test_labels_and_title(self):
        """Verify the labels and the title of the plotted bar chart."""
        random.seed(2)
        _ = task_func(15)
        fig = plt.gcf()
        axes = fig.gca()
        self.assertEqual(axes.get_xlabel(), 'Letter:Number Pairs', 'X label is incorrect.')
        self.assertEqual(axes.get_ylabel(), 'Counts', 'Y label is incorrect.')
        self.assertEqual(axes.get_title(), 'Random Letter:Number Pairs Chart', 'Title is incorrect.')
