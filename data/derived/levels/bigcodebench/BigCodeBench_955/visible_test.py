from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.axes

class TestCases(unittest.TestCase):

    def test_case_1(self):
        ax = task_func(['hello'], 'Hello world!')
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        xtick_labels = [label.get_text() for label in ax.get_xticklabels()]
        self.assertTrue('hello' in xtick_labels)
        self.assertTrue('world!' in xtick_labels)
        self.assertEqual(ax.patches[0].get_height(), 1)

    def test_case_2(self):
        ax = task_func(['hello world'], 'Hello world!')
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(ax.get_xticklabels()[0].get_text(), 'hello_world!')
        self.assertEqual(ax.patches[0].get_height(), 1)

    def test_case_3(self):
        ax = task_func([], 'Hello world!')
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        xtick_labels = [label.get_text() for label in ax.get_xticklabels()]
        self.assertTrue('Hello' in xtick_labels)
        self.assertTrue('world!' in xtick_labels)
        self.assertEqual(ax.patches[0].get_height(), 1)
