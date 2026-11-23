from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def _check_plot_structure(self, ax):
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Average Student Scores')
        self.assertEqual(ax.get_xlabel(), 'Student')
        self.assertEqual(ax.get_ylabel(), 'Average Score')

    def test_case_1(self):
        data = [{'John': 5, 'Jane': 10, 'Joe': 7}, {'John': 6, 'Jane': 8, 'Joe': 10}, {'John': 5, 'Jane': 9, 'Joe': 8}, {'John': 7, 'Jane': 10, 'Joe': 9}]
        ax = task_func(data)
        self._check_plot_structure(ax)
        for bar, label in zip(ax.containers[0], ['Jane', 'Joe', 'John']):
            if label == 'Jane':
                self.assertEqual(bar.get_height(), 9.25)
            elif label == 'Joe':
                self.assertEqual(bar.get_height(), 8.5)
            elif label == 'John':
                self.assertEqual(bar.get_height(), 5.75)

    def test_case_2(self):
        data = [{'John': 5}, {'John': 6}, {'John': 7}, {'John': 8}]
        ax = task_func(data)
        self._check_plot_structure(ax)
        for bar, _ in zip(ax.containers[0], ['John']):
            self.assertEqual(bar.get_height(), 6.5)

    def test_case_3(self):
        data = [{'John': 10}, {'Jane': 15}, {'Joe': 20}]
        ax = task_func(data)
        self._check_plot_structure(ax)
        expected_scores = {'Jane': 15, 'Joe': 20, 'John': 10}
        for bar, label in zip(ax.containers[0], expected_scores.keys()):
            self.assertEqual(bar.get_height(), expected_scores[label])

    def tearDown(self):
        plt.close('all')
