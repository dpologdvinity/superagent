from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from matplotlib import colors as mcolors
from matplotlib.figure import Figure
import doctest

class TestCases(unittest.TestCase):

    def test_standard_normal_distribution(self):
        """Test with standard normal distribution parameters (mu=0, sigma=1)."""
        fig = task_func(0, 1)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])

    def test_nonzero_mean(self):
        """Test with a nonzero mean."""
        mu = 5
        sigma = 1
        fig = task_func(mu, sigma)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])

    def test_different_standard_deviation(self):
        """Test with a different standard deviation."""
        mu = 0
        sigma = 2
        fig = task_func(mu, sigma)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])

    def _test_histogram_attributes(self, ax, expected_bins, color):
        """Helper function to test histogram attributes."""
        n, bins, patches = ax.hist([], bins=expected_bins, color=color)
        self.assertEqual(expected_bins, len(patches))
        self.assertEqual(patches[0].get_facecolor(), mcolors.to_rgba(color))

    def _test_qq_plot_attributes(self, ax):
        """Helper function to test Q-Q plot attributes."""
        self.assertTrue(len(ax.get_lines()) > 0)
