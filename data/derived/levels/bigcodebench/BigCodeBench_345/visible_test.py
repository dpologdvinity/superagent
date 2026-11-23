from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_numeric_data(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]})
        ax = task_func(df, 'A', 'B')
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes, 'The returned object should be a seaborn FacetGrid.')
        plt.close()

    def test_non_numeric_data(self):
        df = pd.DataFrame({'A': ['one', 'two', 'three', 'four', 'five'], 'B': ['five', 'four', 'three', 'two', 'one']})
        with self.assertRaises(TypeError, msg='The function should raise a TypeError for non-numeric data.'):
            task_func(df, 'A', 'B')
        plt.close()

    def test_missing_data(self):
        df = pd.DataFrame({'A': [1, 2, None, 4, 5], 'B': [5, None, 3, 2, 1]})
        ax = task_func(df, 'A', 'B')
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes, 'The returned object should be a seaborn FacetGrid.')
        non_na_length = df.dropna().shape[0]
        self.assertEqual(len(ax.collections[0].get_offsets().data), non_na_length)
        plt.close()
