from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import numpy as np

class TestCases(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=COLUMNS)
        self.tuples = [self.df.iloc[0].values, self.df.iloc[1].values]

    def test_no_plots_generated(self):
        """Test case with zero plots requested."""
        _, plots = task_func(self.df, [], 0)
        self.assertEqual(len(plots), 0, 'No plots should be generated when n_plots is 0.')

    def test_plot_generation(self):
        _, plots = task_func(self.df, [], 3)
        self.assertEqual(len(plots), 3, 'Should generate exactly 3 plots.')

    @patch('matplotlib.pyplot.show')
    def test_empty_dataframe(self, mock_show):
        empty_df = pd.DataFrame(columns=COLUMNS)
        modified_df, plots = task_func(empty_df, [], 2)
        self.assertTrue(modified_df.empty, 'DataFrame should be empty.')
        self.assertEqual(len(plots), 2, 'Should attempt to generate 2 plots even for an empty DataFrame.')
