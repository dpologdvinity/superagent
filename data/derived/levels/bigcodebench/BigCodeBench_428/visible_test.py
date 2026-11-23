from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6], 'feature2': [2.3, 4.5, 6.7], 'feature3': [3.4, 5.6, 7.8]})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'feature4': [4.5, 6.7, 8.9], 'feature5': [5.6, 7.8, 9.0]})
        scaled_df, _ = task_func(df1, df2)
        self.assertEqual(list(scaled_df.columns), ['id', 'feature1', 'feature2', 'feature3', 'feature4', 'feature5'])
        self.assertAlmostEqual(scaled_df['feature1'].mean(), 0, places=5)

    def test_case_2(self):
        df1 = pd.DataFrame({'id': [1, 3, 5], 'feature1': [10, 20, 30], 'feature2': [5, 15, 25], 'feature3': [6, 16, 26]})
        df2 = pd.DataFrame({'id': [1, 5, 3], 'feature4': [7, 17, 27], 'feature5': [8, 18, 28]})
        scaled_df, _ = task_func(df1, df2)
        self.assertAlmostEqual(scaled_df['feature2'].std(), 1.224745, places=5)

    def test_case_3(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [-1, -2, -3], 'feature2': [-5, -6, -7], 'feature3': [-8, -9, -10]})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'feature4': [-11, -12, -13], 'feature5': [-14, -15, -16]})
        scaled_df, _ = task_func(df1, df2)
        self.assertAlmostEqual(scaled_df['feature3'].max(), 1.224745, places=5)

    def tearDown(self):
        plt.close('all')
