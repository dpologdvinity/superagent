from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
from collections import Counter
import tempfile
import shutil
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store plots
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Close matplotlib plots and remove temporary directory
        plt.close("all")
    def test_case_1(self):
        # Test basic functionality with 100 rolls and 2 dice
        result, ax = task_func(100, 2, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_2(self):
        # Test plot saving functionality
        plot_path = os.path.join(self.test_dir, "test_plot.png")
        result, ax = task_func(1000, 1, plot_path, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(os.path.exists(plot_path))
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_3(self):
        # Test with a larger number of dice
        result, ax = task_func(500, 5, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_4(self):
        # Test with the minimum possible inputs
        result, ax = task_func(1, 1, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(len(result), 1)  # Only one possible sum with 1 roll of 1 die
    def test_case_5(self):
        # Test the effect of different random seeds on the result consistency
        result1, _ = task_func(100, 2, random_seed=42)
        result2, _ = task_func(100, 2, random_seed=43)
        self.assertNotEqual(
            result1, result2, "Results should differ with different seeds"
        )
    def test_case_6(self):
        # Test plot detail correctness (labels, title)
        plot_path = os.path.join(self.test_dir, "test_plot_detail.png")
        _, ax = task_func(10, 2, plot_path, random_seed=42)
        self.assertTrue(
            "sum of dice roll" in ax.get_xlabel().lower(), "X-axis label is incorrect"
        )
        self.assertEqual(ax.get_ylabel(), "Count", "Y-axis label is incorrect")
        self.assertTrue(
            "distribution of dice roll sums" in ax.get_title().lower(),
            "Plot title is incorrect",
        )
    def test_case_7(self):
        # Test data correctness with a manually calculated example
        result, _ = task_func(2, 1, random_seed=42)
        expected = Counter({6: 1, 1: 1})
        self.assertEqual(
            result, expected, "Data distribution does not match expected outcome"
        )
    def tearDown(self):
        plt.close("all")
