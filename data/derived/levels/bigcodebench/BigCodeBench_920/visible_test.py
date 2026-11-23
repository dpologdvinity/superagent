from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')

    def test_case_2(self):
        data = {'a': [1, 2, 3], 'b': [-4, -5, -6], 'c': [-7, -8, -9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')

    def test_case_3(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [-7, -8, -9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
