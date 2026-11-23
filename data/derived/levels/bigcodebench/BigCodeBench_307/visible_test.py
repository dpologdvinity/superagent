from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        plot = task_func([[1, 2, 3], [], [4, 5, 6]])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
        self.assertEqual(len(plot.patches), 5)

    def test_case_2(self):
        plot = task_func([[], [], []])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")

    def test_case_3(self):
        plot = task_func([[1, 2, 3, 4, 5]], 77)
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
        self.assertEqual(len(plot.patches), 4)
