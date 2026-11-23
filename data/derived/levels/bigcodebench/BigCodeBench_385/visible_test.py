from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.axes
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        fruit_dict = {'John': 'Apple', 'Alice': 'Banana', 'Bob': 'Cherry'}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {'Apple': 1, 'Banana': 1, 'Cherry': 1})
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_case_2(self):
        fruit_dict = {'John': 'Apple', 'Alice': 'Banana', 'Bob': 'Apple'}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {'Apple': 2, 'Banana': 1})
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_case_3(self):
        fruit_dict = {}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {})
        self.assertIsInstance(ax, matplotlib.axes.Axes)
