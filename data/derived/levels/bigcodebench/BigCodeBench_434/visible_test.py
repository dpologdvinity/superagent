from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        self.df1 = pd.DataFrame({'ID': ['1'], 'Quantity': ['10'], 'Code': ['A10B'], 'Price': ['100'], 'Description': ['This is a description with spaces']})
        self.df2 = pd.DataFrame({'ID': ['2'], 'Quantity': ['15'], 'Code': ['B20C'], 'Price': ['200'], 'Description': ['Another description with spaces']})
        self.df_multiple = pd.concat([self.df1, self.df2]).reset_index(drop=True)
        for col in ['Quantity', 'Price']:
            self.df1[col] = self.df1[col].astype(int)
            self.df2[col] = self.df2[col].astype(int)
            self.df_multiple[col] = self.df_multiple[col].astype(int)

    def _test_most_columns(self, df1, df2):
        columns_to_test = ['ID', 'Quantity', 'Code', 'Price', 'Description']
        for col in columns_to_test:
            pd.testing.assert_series_equal(df1[col], df2[col])

    def test_case_1(self):
        input_str = '1 10 A10B 100 This is a description with spaces'
        result = task_func(input_str)
        self.assertIsInstance(result, pd.DataFrame)
        self._test_most_columns(result, self.df1)

    def test_case_2(self):
        input_str = '\n'.join(['1 10 A10B 100 This is a description with spaces', '2 15 B20C 200 Another description with spaces'])
        result = task_func(input_str)
        self._test_most_columns(result, self.df_multiple)

    def test_case_3(self):
        input_str = '\n'.join(['1 10 A10B 100 This is a description with spaces         ', '2 15 B20C 200 Another description with spaces     '])
        result = task_func(input_str)
        self._test_most_columns(result, self.df_multiple)
