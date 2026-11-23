from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
        result = task_func(df, dct)
        self.assertTrue(result.shape == (2, 2))

    def test_case_2(self):
        df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
        dct = {1: 10, 2: 20, 4: 40, 6: 60}
        result = task_func(df, dct)
        self.assertTrue(result.isna().sum().sum() > 0)

    def test_case_3(self):
        df = pd.DataFrame({'A': [-1, -2, -3], 'B': [-4, -5, -6]})
        dct = {-1: 1, -2: 2, -3: 3, -4: 4, -5: 5, -6: 6}
        result = task_func(df, dct)
        self.assertTrue(result.shape == (2, 2))
