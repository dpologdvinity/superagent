from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
from unittest.mock import patch

class TestCases(unittest.TestCase):

    @patch('time.sleep', return_value=None)
    def test_case_1(self, mock_sleep):
        ax, kurtosis = task_func(5)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 5)
        self.assertEqual(len(lines[0].get_ydata()), 5)
        self.assertEqual(mock_sleep.call_count, 5)

    @patch('time.sleep', return_value=None)
    def test_case_2(self, mock_sleep):
        ax, kurtosis = task_func(10, 44)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 10)
        self.assertEqual(len(lines[0].get_ydata()), 10)
        self.assertNotAlmostEqual(kurtosis, -0.34024, places=5)

    @patch('time.sleep', return_value=None)
    def test_case_3(self, mock_sleep):
        ax, kurtosis = task_func()
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 100)
        self.assertEqual(len(lines[0].get_ydata()), 100)
