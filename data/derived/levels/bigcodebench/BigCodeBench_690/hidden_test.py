from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
    
    def test_case_2(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
    def test_case_3(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
    def test_case_4(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) is not None)
    def test_case_5(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) >= 0)
