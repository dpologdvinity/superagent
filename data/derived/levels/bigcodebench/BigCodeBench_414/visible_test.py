from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        np.random.seed(0)
        data = {'a': np.random.randn(10), 'b': np.random.randn(10), 'c': np.random.randn(10)}
        df = pd.DataFrame(data)
        modified_df, ax = task_func(data)
        self.assertNotIn('c', modified_df.columns)
        plotted_data = [line.get_ydata() for line in ax.get_lines()]
        self.assertTrue(all([np.array_equal(data, modified_df[col].values) for data, col in zip(plotted_data, modified_df.columns)]))

    def test_case_2(self):
        np.random.seed(0)
        data = {'a': np.random.randn(10), 'b': np.random.randn(10)}
        df = pd.DataFrame(data)
        modified_df, ax = task_func(data)
        self.assertEqual(list(df.columns), list(modified_df.columns))
        self.assertIsNotNone(ax)

    def test_case_3(self):
        data = {}
        df = pd.DataFrame(data)
        modified_df, ax = task_func(data)
        self.assertTrue(modified_df.empty)
        self.assertIsNone(ax)

    def tearDown(self):
        plt.close('all')
