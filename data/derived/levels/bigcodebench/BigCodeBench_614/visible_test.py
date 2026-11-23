from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch

class TestCases(unittest.TestCase):

    @patch('matplotlib.pyplot.show')
    def test_visualization_output(self, mock_show):
        goals = {'Team A': 3, 'Team B': 2, 'Team C': 0}
        penalties = {'Team A': 1, 'Team B': 0, 'Team C': 2}
        df, _ = task_func(goals, penalties)
        self.assertEqual(list(df.columns), ['Team', 'Goals', 'Penalties'])
        self.assertEqual(df['Goals'].sum(), 5)
        self.assertEqual(df['Penalties'].sum(), 3)

    def test_empty_input(self):
        goals = {}
        penalties = {}
        df, _ = task_func(goals, penalties)
        expected_data = {'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'], 'Goals': [0, 0, 0, 0, 0], 'Penalties': [0, 0, 0, 0, 0]}
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df, expected_df)

    def test_plot_type(self):
        goals = {'Team A': 1}
        penalties = {'Team A': 1}
        _, plot = task_func(goals, penalties)
        self.assertIsInstance(plot, sns.axisgrid.PairGrid)
