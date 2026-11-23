from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def tearDown(self):
        plt.close('all')

    def test_case_1(self):
        df1 = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'feature1': [5.5, 6.7, 7.8, 8.9, 9.0], 'feature2': [1.1, 2.2, 3.3, 4.4, 5.5], 'feature3': [0.5, 1.5, 2.5, 3.5, 4.5]})
        df2 = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'target': [1, 0, 1, 0, 1]})
        selected_features, ax = task_func(df1, df2)
        self.assertListEqual(selected_features, ['feature1', 'feature3'])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())

    def test_case_2(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6], 'feature2': [2.3, 4.5, 6.7], 'feature3': [3.4, 5.6, 7.8]})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'target': [4.5, 6.7, 8.9]})
        selected_features, ax = task_func(df1, df2)
        self.assertListEqual(selected_features, ['feature2', 'feature3'])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())

    def test_case_3(self):
        df1 = pd.DataFrame({'id': [1, 2, 3, 4], 'feature1': [2.5, 3.5, 4.5, 5.5], 'feature2': [6.6, 7.7, 8.8, 9.9], 'feature3': [10.1, 11.1, 12.1, 13.1]})
        df2 = pd.DataFrame({'id': [1, 2, 3, 4], 'target': [0, 1, 0, 1]})
        selected_features, ax = task_func(df1, df2)
        self.assertListEqual(selected_features, ['feature2', 'feature3'])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
