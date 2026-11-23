from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from collections import Counter
import matplotlib

class TestCases(unittest.TestCase):

    def _check_plot(self, ax):
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Distribution')
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')

    def test_case_1(self):
        df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
        counter, ax = task_func(df)
        self._check_plot(ax)
        self.assertEqual(counter, Counter())

    def test_case_2(self):
        df = pd.DataFrame({'value': [1, 1, 1, 1, 1]})
        counter, ax = task_func(df)
        self._check_plot(ax)
        self.assertEqual(counter, Counter({1: 5}))

    def test_case_3(self):
        df = pd.DataFrame({'value': []})
        counter, ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(counter, Counter())

    def tearDown(self):
        plt.close('all')
