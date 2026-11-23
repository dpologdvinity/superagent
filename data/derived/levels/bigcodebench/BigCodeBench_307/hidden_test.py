from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input: Two non-empty sublists and one empty sublist
        plot = task_func([[1, 2, 3], [], [4, 5, 6]])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
        # Test the number of bars in the histogram
        self.assertEqual(len(plot.patches), 5)
    def test_case_2(self):
        # Input: All empty sublists
        plot = task_func([[], [], []])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
    def test_case_3(self):
        # Input: Single non-empty sublist
        plot = task_func([[1, 2, 3, 4, 5]], 77)
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
        # Test the number of bars in the histogram
        self.assertEqual(len(plot.patches), 4)
    def test_case_4(self):
        # Input: Single empty sublist
        plot = task_func([[]])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
    def test_case_5(self):
        # Input: Mixed empty and non-empty sublists
        plot = task_func([[10, 20], [], [30, 40, 50], []])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
