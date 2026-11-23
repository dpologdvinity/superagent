from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def setUp(self):
        self.columns = ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5']
        np.random.seed(0)

    def test_case_1(self):
        data = pd.DataFrame(np.random.rand(100, 5), columns=self.columns)
        self.standardized_data_test(data)

    def test_case_2(self):
        data = pd.DataFrame(np.random.exponential(scale=1.0, size=(100, 5)), columns=self.columns)
        self.standardized_data_test(data)

    def test_case_3(self):
        data_1 = np.random.rand(100, 3)
        data_2 = np.random.exponential(scale=1.0, size=(100, 2))
        data = pd.DataFrame(np.hstack((data_1, data_2)), columns=self.columns)
        self.standardized_data_test(data)

    def standardized_data_test(self, data):
        np.random.seed(0)
        standardized_data, axes_list = task_func(data)
        self.assertTrue(np.isclose(standardized_data.mean().values, 0, atol=0.01).all())
        self.assertTrue(np.isclose(standardized_data.std().values, 1, atol=0.1).all())
        self.assertEqual(len(axes_list), 5)
        for ax, feature in zip(axes_list, self.columns):
            self.assertEqual(ax.get_title(), f'Histogram of {feature}')
        for ax in axes_list:
            self.assertEqual(len(ax.patches), 20)

    def tearDown(self):
        plt.close('all')
