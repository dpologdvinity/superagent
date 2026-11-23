from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        ax, _, _ = task_func()
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Normal Distribution with $\\mu = 0.00, \\sigma = 1.00$')

    def test_case_2(self):
        ax, mean, std = task_func(mu=5, sigma=2, sample_size=500, seed=42)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Normal Distribution with $\\mu = 5.00, \\sigma = 2.00$')
        self.assertAlmostEqual(mean, 5.0136, places=3)

    def test_case_3(self):
        ax, mean, std = task_func(mu=-3, sigma=5, sample_size=2000, seed=23)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Normal Distribution with $\\mu = -3.00, \\sigma = 5.00$')
        self.assertAlmostEqual(std, 4.978, places=3)
