from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def tearDown(self):
        plt.close('all')

    def test_cumsum_correctness(self):
        data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        df = pd.DataFrame(data)
        ax = task_func(data)
        result_cumsum = df.cumsum().values.flatten()
        heatmap_data = ax.collections[0].get_array().data.flatten()
        np.testing.assert_array_equal(result_cumsum, heatmap_data, 'Cumulative sum calculation is incorrect')

    def test_non_numeric_columns_ignored(self):
        data = {'A': [1, 2, 3], 'B': ['one', 'two', 'three']}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes, 'The result should be a matplotlib Axes object')
        self.assertEqual(len(ax.get_xticklabels()), 1, 'Non-numeric columns should be ignored')

    def test_with_positive_numbers(self):
        data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        result = task_func(data)
        self.assertIsInstance(result, plt.Axes, 'The result should be a matplotlib Axes object')
