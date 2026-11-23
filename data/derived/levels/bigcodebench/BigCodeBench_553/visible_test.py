from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib

class TestCases(unittest.TestCase):

    def test_non_empty_lists(self):
        """Test with valid non-empty lists."""
        ax = task_func([1, 2, 3], ['A', 'B', 'C'])
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_empty_a_list(self):
        """Test with an empty 'a' list."""
        ax = task_func([], ['A', 'B', 'C'])
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_empty_b_list(self):
        """Test with an empty 'b' list."""
        ax = task_func([1, 2, 3], [])
        self.assertIsInstance(ax, matplotlib.axes.Axes)
