from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib

class TestCases(unittest.TestCase):

    def test_standard_functionality(self):
        """Test with typical list inputs."""
        a = ['apple', 'banana', 'cherry']
        b = ['banana', 'apple', 'apple', 'dragonfruit']
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)

    def test_empty_lists(self):
        """Test with both lists empty."""
        a = []
        b = []
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)

    def test_one_empty_list(self):
        """Test with one list empty."""
        a = ['apple', 'apple']
        b = []
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
