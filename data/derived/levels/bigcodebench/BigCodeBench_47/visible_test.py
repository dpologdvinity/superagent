from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    def test_case_1(self):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, None, 9]], columns=['c1', 'c2', 'c3'])
        expected_df = df.copy()
        expected_df = expected_df.fillna(df.mean(axis=0))
        scaler = StandardScaler()
        expected_df[expected_df.columns] = scaler.fit_transform(expected_df[expected_df.columns])
        standardized_df, heatmap = task_func(df)
        pd.testing.assert_frame_equal(standardized_df, expected_df)
        self.assertEqual(standardized_df.shape, df.shape)
        self.assertIsInstance(heatmap, plt.Axes)

    def test_case_2(self):
        df = pd.DataFrame([[3, 7, 9], [4, 1, 8], [2, 6, 5]], columns=['c1', 'c2', 'c3'])
        standardized_df, heatmap = task_func(df)
        self.assertEqual(standardized_df.shape, df.shape)
        self.assertIsInstance(heatmap, plt.Axes)

    def test_case_3(self):
        df = pd.DataFrame([[4, 6, 8], [9, 5, 2], [3, 1, 7]], columns=['c1', 'c2', 'c3'])
        standardized_df, heatmap = task_func(df)
        self.assertEqual(standardized_df.shape, df.shape)
        self.assertIsInstance(heatmap, plt.Axes)
