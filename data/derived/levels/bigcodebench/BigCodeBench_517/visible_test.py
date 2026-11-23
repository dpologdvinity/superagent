from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np

class TestCases(unittest.TestCase):

    def test_case_1(self):
        data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        df, transformed_data = task_func(data)
        expected_df = pd.DataFrame(data)
        self.assertTrue(df.equals(expected_df))
        self.assertEqual(transformed_data.shape, (2, 2))

    def test_case_2(self):
        data = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]]
        df, transformed_data = task_func(data)
        expected_df = pd.DataFrame(data)
        self.assertTrue(df.equals(expected_df))
        self.assertEqual(transformed_data.shape, (3, 2))

    def test_case_3(self):
        data = [[-1, -2, -3, -4, -5], [5, 6, 7, 8, 9], [0, 0, 0, 0, 0]]
        df, transformed_data = task_func(data)
        expected_df = pd.DataFrame(data)
        self.assertTrue(df.equals(expected_df))
        self.assertEqual(transformed_data.shape, (3, 2))
