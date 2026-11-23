from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from matplotlib import pyplot as plt

class TestCases(unittest.TestCase):

    def test_with_all_categories(self):
        """Test with all categories present."""
        data = {'Category': ['A', 'B', 'B', 'C', 'A', 'D', 'E', 'E', 'D']}
        ax = task_func(data, 'Category')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_xlabel(), 'Category')
        self.assertEqual(ax.get_ylabel(), 'Count')
        self.assertEqual(ax.get_title(), 'Distribution of Category')
        self.assertEqual(len(ax.get_xticks()), 5)

    def test_with_missing_categories(self):
        """Test with some categories missing."""
        data = {'Category': ['A', 'A', 'B', 'C']}
        ax = task_func(data, 'Category')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.get_xticks()), 5)

    def test_with_unexpected_category(self):
        """Test with a category not in predefined list."""
        data = {'Category': ['F', 'A', 'B']}
        ax = task_func(data, 'Category')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.get_xticks()), 5)
