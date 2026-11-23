from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with three points where the third point has the highest y-value
        ax, _ = task_func([(0.1, 0.2), (0.5, 0.6), (0.3, 0.9)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        
    def test_case_2(self):
        # Testing with another set of points
        ax, _ = task_func([(0.2, 0.3), (0.6, 0.7), (0.4, 0.8)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        
    def test_case_3(self):
        # Testing with another set of points
        ax, max_y_point = task_func([(0.3, 0.4), (0.7, 0.8), (0.5, 0.7)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertEqual(max_y_point, (0.7, 0.8))
        
    def test_case_4(self):
        # Testing with another set of points
        ax, max_y_point = task_func([(0.4, 0.5), (0.8, 0.9), (0.6, 0.6)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertEqual(max_y_point, (0.8, 0.9))
    def test_case_5(self):
        # Testing with another set of points
        ax, max_y_point = task_func([(0.5, 0.6), (0.9, 0.1), (0.7, 0.5)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertEqual(max_y_point, (0.5, 0.6))
