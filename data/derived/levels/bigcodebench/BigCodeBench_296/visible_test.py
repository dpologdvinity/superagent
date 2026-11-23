from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_normal_dataframe(self):
        df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3], 'value': ['A', 'B', 'A', 'B', 'A', 'B']})
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes, 'Should return an Axes object')
        self.assertEqual(len(ax.patches), 2, "Should have 2 bars for values 'A' and 'B'")
        self.assertEqual(ax.get_title(), 'Value Distribution', 'Incorrect title')
        plt.close()

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['id', 'value'])
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes, 'Should handle empty DataFrame')
        self.assertEqual(len(ax.patches), 0, 'Should have no bars for an empty DataFrame')
        plt.close()

    def test_numeric_values(self):
        df = pd.DataFrame({'id': [1, 2, 3], 'value': [100, 200, 300]})
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes, "Should handle numeric values in 'value' column")
        plt.close()
