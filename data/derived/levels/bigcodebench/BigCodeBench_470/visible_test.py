from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        myList = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        ax = task_func(myList)
        heights, _, _ = ax.hist(myList, bins=np.arange(min(myList), max(myList) + 2) - 0.5, edgecolor='black')
        self.assertIsInstance(ax, plt.Axes)
        self.assertListEqual(list(heights), [1, 2, 3, 4])
        self.assertEqual(ax.get_title(), 'Histogram of Values')
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')

    def test_case_2(self):
        with self.assertRaises(ValueError):
            task_func([])

    def test_case_3(self):
        myList = [100]
        ax = task_func(myList)
        heights, _, _ = ax.hist(myList)
        self.assertEqual(heights.max(), 1)

    def tearDown(self):
        plt.close('all')
