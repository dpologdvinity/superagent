from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np

class TestCases(unittest.TestCase):

    def setUp(self):
        self.valid_df = pd.DataFrame({'group': ['A', 'A', 'A', 'B', 'B'], 'date': pd.to_datetime(['2022-01-02', '2022-01-13', '2022-02-01', '2022-02-23', '2022-03-05']), 'value': [10, 20, 16, 31, 56]})

    def test_valid_input(self):
        heatmap_fig, pairplot_grid = task_func(self.valid_df)
        self.assertIsInstance(heatmap_fig, plt.Figure)
        self.assertIsInstance(pairplot_grid, sns.axisgrid.PairGrid)

    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame())

    def test_missing_columns(self):
        incomplete_df = self.valid_df.drop(columns=['date'])
        with self.assertRaises(ValueError):
            task_func(incomplete_df)
