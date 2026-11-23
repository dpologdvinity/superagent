from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        cumsum, ax = task_func([10, 20, 30])
        self.assertListEqual(list(cumsum), [10, 30, 60])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_2(self):
        cumsum, ax = task_func([5, 15, 25])
        self.assertListEqual(list(cumsum), [5, 20, 45])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_3(self):
        cumsum, ax = task_func([])
        self.assertListEqual(list(cumsum), [])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_4(self):
        cumsum, ax = task_func([1, 2, 3, 4, 5])
        self.assertListEqual(list(cumsum), [1, 3, 6, 10, 15])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_5(self):
        cumsum, ax = task_func([5])
        self.assertListEqual(list(cumsum), [5])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
