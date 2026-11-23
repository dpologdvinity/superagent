from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df = pd.DataFrame({'feature': np.random.rand(100), 'value': np.random.rand(100)})
        coefficients = task_func(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)

    def test_case_2(self):
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [1, 2, 3, 4, 5]})
        coefficients = task_func(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
        self.assertAlmostEqual(coefficients['coefficients'][0][0], 1.0)
        self.assertAlmostEqual(coefficients['intercept'][0], 0.0)

    def test_case_3(self):
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [2, 4, 6, 8, 10]})
        coefficients = task_func(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
        self.assertAlmostEqual(coefficients['coefficients'][0][0], 2.0)
        self.assertAlmostEqual(coefficients['intercept'][0], 0.0)
