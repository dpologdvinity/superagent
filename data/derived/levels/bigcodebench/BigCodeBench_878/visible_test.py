from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np
from faker import Faker
from sklearn.ensemble import RandomForestRegressor

class TestCases(unittest.TestCase):

    def setUp(self) -> None:
        self.fake = Faker()

    def test_case_1(self):
        data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'target': [10, 11, 12]}
        mse, model, df = task_func(data, 'target', random_state=2)
        self.assertAlmostEqual(mse, 1.537, delta=0.2)
        self.assertTrue(isinstance(model, RandomForestRegressor))
        pd.testing.assert_frame_equal(pd.DataFrame(data), df)

    def test_case_2(self):
        np.random.seed(42)
        data = {'A': np.random.randint(0, 100), 'B': np.random.randint(0, 100), 'C': np.random.randint(0, 100), 'D': np.random.randint(0, 100)}
        data['target'] = np.random.randint(0, 100, size=(100,))
        mse, model, df = task_func(data, 'target', random_state=12)
        self.assertAlmostEqual(mse, 1012, delta=20)
        self.assertTrue(isinstance(model, RandomForestRegressor))
        pd.testing.assert_frame_equal(pd.DataFrame(data), df)

    def test_case_3(self):
        np.random.seed(42)
        data = {'A': np.random.randint(0, 100), 'B': np.random.randint(0, 100), 'C': np.random.randint(0, 100), 'D': np.random.randint(0, 100)}
        data['target'] = np.random.randint(0, 100, size=(100,))
        mse, model, df = task_func(data, 'target', test_size=0.3, random_state=12)
        self.assertAlmostEqual(mse, 1048, delta=20)
        self.assertTrue(isinstance(model, RandomForestRegressor))
        pd.testing.assert_frame_equal(pd.DataFrame(data), df)
