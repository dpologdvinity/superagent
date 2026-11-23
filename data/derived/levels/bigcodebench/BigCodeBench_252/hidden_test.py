from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
        labels = ['Series 1', 'Series 2', 'Series 3']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[0].get_color(), 'red')
        self.assertEqual(lines[1].get_color(), 'green')
        self.assertEqual(lines[2].get_color(), 'blue')
    def test_case_2(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        labels = ['A', 'B', 'C', 'D']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[3].get_color(), 'yellow')
    def test_case_3(self):
        data = [[1, 2], [3, 4]]
        labels = ['X', 'Y']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[0].get_color(), 'red')
        self.assertEqual(lines[1].get_color(), 'green')
    def test_case_4(self):
        data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
        labels = ['Series 1', 'Series 2', 'Series 3', 'Series 4', 'Series 5', 'Series 6']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[5].get_color(), 'black')
        
    def test_case_5(self):
        data = [[1, 2, 3], [4, 5, 6]]
        labels = []
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[0].get_color(), 'red')
        self.assertEqual(lines[1].get_color(), 'green')
