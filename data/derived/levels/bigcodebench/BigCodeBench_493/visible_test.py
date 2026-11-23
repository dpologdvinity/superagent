from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def setUp(self):
        self.x = 1631295600000
        self.default_valid_teams = ['Team1', 'Team2', 'Team3', 'Team4', 'Team5']

    def _check_valid_performance_data(self, performance_data, valid_teams):
        self.assertIsInstance(performance_data, dict)
        self.assertTrue(all((team in valid_teams for team in performance_data.keys())))
        for team, performances in performance_data.items():
            for performance in performances:
                self.assertTrue(0.1 <= performance <= 1, f'Performance out of range for {team}')
                self.assertIsInstance(performance, float)

    def _check_plot(self, fig):
        ax = fig.axes[0]
        self.assertIsInstance(fig, plt.Figure)
        self.assertEqual(ax.get_ylabel(), 'Performance')
        self.assertTrue(ax.get_xlabel().startswith('Days since'))

    def test_case_1(self):
        performance_data, _ = task_func(self.x)
        self._check_valid_performance_data(performance_data, self.default_valid_teams)

    def test_case_2(self):
        _, fig = task_func(self.x)
        self._check_plot(fig)

    def test_case_3(self):
        performance_data, fig = task_func(1236472051807, random_seed=42)
        self._check_plot(fig)
        self._check_valid_performance_data(performance_data, self.default_valid_teams)

    def tearDown(self):
        plt.close('all')
