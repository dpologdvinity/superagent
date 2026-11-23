from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import pandas as pd
import unittest
import matplotlib
matplotlib.use('Agg')

class TestCases(unittest.TestCase):

    def test_case_1(self):
        data_1 = pd.DataFrame({'Title': ['How to code?', 'What is Python?', 'The art of programming', 'How to cook?', 'What is life?'], 'Views': [1000, 500, 200, 300, 800], 'Likes': [500, 250, 100, 150, 600]})
        ax = task_func(data_1)
        self.assertIsInstance(ax, matplotlib.axes.Axes, 'The returned object should be of type Axes.')
        y_data = [rect.get_height() for rect in ax.patches]
        expected_y_data = [0.5, 0.5, 0.5, 0.75]
        self.assertEqual(y_data, expected_y_data, f'Expected {expected_y_data}, but got {y_data}')

    def test_case_2(self):
        data_2 = pd.DataFrame({'Title': ['How to swim?', 'What is Java?', 'The beauty of nature', 'How to paint?', 'What is art?'], 'Views': [1200, 400, 250, 350, 900], 'Likes': [600, 200, 125, 175, 450]})
        ax = task_func(data_2)
        self.assertIsInstance(ax, matplotlib.axes.Axes, 'The returned object should be of type Axes.')
        y_data = [rect.get_height() for rect in ax.patches]
        expected_y_data = [0.5, 0.5, 0.5, 0.5]
        self.assertEqual(y_data, expected_y_data, f'Expected {expected_y_data}, but got {y_data}')

    def test_case_3(self):
        data_3 = pd.DataFrame({'Title': [], 'Views': [], 'Likes': []})
        ax = task_func(data_3)
        self.assertIsInstance(ax, matplotlib.axes.Axes, 'The returned object should be of type Axes.')
