from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        activities = [datetime(2023, 10, 23), datetime(2023, 10, 24)]
        ax = task_func(activities)
        bars = ax.patches
        self.assertEqual(ax.get_title(), 'Weekly Activity')
        self.assertEqual(ax.get_xlabel(), 'Day of the Week')
        self.assertEqual(ax.get_ylabel(), 'Number of Activities')
        self.assertEqual(bars[0].get_height(), 1)
        self.assertEqual(bars[1].get_height(), 1)
        for i in range(2, 7):
            self.assertEqual(bars[i].get_height(), 0)

    def test_case_2(self):
        activities = [datetime(2023, 10, 23), datetime(2023, 10, 24), datetime(2023, 10, 24), datetime(2023, 10, 26)]
        ax = task_func(activities)
        bars = ax.patches
        self.assertEqual(ax.get_title(), 'Weekly Activity')
        self.assertEqual(ax.get_xlabel(), 'Day of the Week')
        self.assertEqual(ax.get_ylabel(), 'Number of Activities')
        self.assertEqual(bars[0].get_height(), 1)
        self.assertEqual(bars[1].get_height(), 2)
        self.assertEqual(bars[2].get_height(), 0)
        self.assertEqual(bars[3].get_height(), 1)
        for i in range(4, 7):
            self.assertEqual(bars[i].get_height(), 0)

    def test_case_3(self):
        activities = [datetime(2023, 10, 29), datetime(2023, 10, 29)]
        ax = task_func(activities)
        bars = ax.patches
        for i in range(0, 6):
            self.assertEqual(bars[i].get_height(), 0)
        self.assertEqual(bars[6].get_height(), 2)
