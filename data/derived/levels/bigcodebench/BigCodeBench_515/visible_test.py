from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

class TestCases(unittest.TestCase):

    def setUp(self):
        random.seed(42)
        self.mock_data = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]

    def test_case_1(self):
        df, _ = task_func(self.mock_data)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (5, 5))

    def test_case_2(self):
        _, heatmap = task_func(self.mock_data)
        self.assertIsNotNone(heatmap)

    def test_case_3(self):
        correlated_data = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
        df, _ = task_func(correlated_data)
        corr_matrix = df.corr()
        np.testing.assert_array_almost_equal(corr_matrix, np.corrcoef(correlated_data, rowvar=False))

    def tearDown(self):
        plt.close('all')
