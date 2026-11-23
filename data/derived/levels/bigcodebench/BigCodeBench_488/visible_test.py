from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        test_cases = [(0, 10000, 100, 1, 1000), (0, 100000, 1000, 2, 5000), (0, 10000, 100, 0.5, 1000), (0, 10000, 100, 1, 500), (0, 10000, 500, 1, 1000)]
        for start_time, end_time, step, amplitude, period in test_cases:
            with self.subTest(start_time=start_time, end_time=end_time, step=step, amplitude=amplitude, period=period):
                ax = task_func(start_time, end_time, step, amplitude, period)
                self.assertIsInstance(ax, plt.Axes)
                self.assertEqual(ax.get_title(), 'Time Series with Seasonality')
                self.assertEqual(ax.get_xlabel(), 'Timestamp')
                self.assertEqual(ax.get_ylabel(), 'Value')

    def test_case_2(self):
        ax = task_func(0, 10000, 200000, 1, 1000)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Time Series with Seasonality')
        self.assertEqual(ax.get_xlabel(), 'Timestamp')
        self.assertEqual(ax.get_ylabel(), 'Value')

    def test_case_3(self):
        with self.assertRaises(ValueError):
            task_func(0, 10000, 100, 1, 0)
        with self.assertRaises(ValueError):
            task_func(0, 10000, 100, 1, -1)

    def tearDown(self):
        plt.close('all')
