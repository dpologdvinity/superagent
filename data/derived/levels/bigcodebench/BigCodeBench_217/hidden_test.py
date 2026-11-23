from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax, _, _ = task_func()
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 0.00, \\sigma = 1.00$")
    def test_case_2(self):
        ax, mean, std = task_func(mu=5, sigma=2, sample_size=500, seed=42)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 5.00, \\sigma = 2.00$")
        self.assertAlmostEqual(mean, 5.0136, places=3)
    def test_case_3(self):
        ax, mean, std = task_func(mu=-3, sigma=5, sample_size=2000, seed=23)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = -3.00, \\sigma = 5.00$")
        self.assertAlmostEqual(std, 4.978, places=3)
    def test_case_4(self):
        ax, _, _ = task_func(mu=1, sigma=0.5, sample_size=100)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 1.00, \\sigma = 0.50$")
    def test_case_5(self):
        ax, mean, std = task_func(mu=10, sigma=0.1, sample_size=1500)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 10.00, \\sigma = 0.10$")
        self.assertAlmostEqual(mean, 9.998, places=3)
        self.assertAlmostEqual(std, 0.09804, places=3)
