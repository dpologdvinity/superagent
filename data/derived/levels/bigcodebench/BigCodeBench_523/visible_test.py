from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class TestCases(unittest.TestCase):

    def setUp(self):
        self.data1 = [{'A': 10, 'B': 15, 'C': 12}, {'A': 12, 'B': 20, 'C': 14}, {'A': 15, 'B': 18, 'C': 15}, {'A': 11, 'B': 17, 'C': 13}]
        self.data2 = [{'X': 5, 'Y': 8}, {'X': 6, 'Y': 7}, {'X': 7, 'Y': 6}, {'X': 8, 'Y': 5}]
        self.data3 = [{'P': 3, 'Q': 2, 'R': 4, 'S': 1}, {'P': 4, 'Q': 3, 'R': 2, 'S': 3}]
        self.data4 = [{'W': 7}, {'W': 8}, {'W': 9}, {'W': 6}]
        self.data5 = [{'M': 1, 'N': 3}, {'M': 3, 'N': 1}]

    def test_case_1(self):
        ax = task_func(self.data1)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(ax.get_title(), 'Data over Time')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Data Points')
        self.assertEqual(len(ax.lines), 3)

    def test_case_2(self):
        data = [{'A': 1, 'B': 2}, {'B': 3, 'C': 4}, {'A': 5, 'C': 6}]
        ax = task_func(data)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertTrue(len(ax.lines) > 0)

    def test_case_3(self):
        self.assertIsNone(task_func([]))

    def tearDown(self):
        plt.close('all')
