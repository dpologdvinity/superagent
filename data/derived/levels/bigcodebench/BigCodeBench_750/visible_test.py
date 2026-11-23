from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        np.random.seed(42)

    def test_case_1(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper)
        self.assertEqual(results.params.index.to_list(), ['const', 'Height', 'Weight'])

    def test_case_2(self):
        df = pd.DataFrame(np.random.randint(30, 40, size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsNone(results)

    def test_case_3(self):
        df = pd.DataFrame(np.random.randint(60, 80, size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper)
        self.assertEqual(results.params.index.to_list(), ['const', 'Height', 'Weight'])
