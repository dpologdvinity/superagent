from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        ax, _ = task_func([(0.1, 0.2), (0.5, 0.6), (0.3, 0.9)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')

    def test_case_2(self):
        ax, _ = task_func([(0.2, 0.3), (0.6, 0.7), (0.4, 0.8)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')

    def test_case_3(self):
        ax, max_y_point = task_func([(0.3, 0.4), (0.7, 0.8), (0.5, 0.7)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertEqual(max_y_point, (0.7, 0.8))
