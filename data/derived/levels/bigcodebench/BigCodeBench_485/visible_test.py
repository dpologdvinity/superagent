from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        ax = task_func('2021-01-01', '2021-01-10')
        self._common_assertions(ax)

    def test_case_2(self):
        ax = task_func('2021-01-01', '2021-01-01')
        self._common_assertions(ax)

    def test_case_3(self):
        ax = task_func('2020-02-28', '2020-03-01')
        self._common_assertions(ax)

    def _common_assertions(self, ax):
        """Common assertions for all test cases"""
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel().lower(), 'time difference (hours)'.lower())
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        expected_timezones = ['UTC', 'America/Los_Angeles', 'Europe/Paris', 'Asia/Kolkata', 'Australia/Sydney']
        self.assertListEqual(legend_labels, expected_timezones)

    def tearDown(self):
        plt.close('all')
