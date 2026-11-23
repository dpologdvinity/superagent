from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        self.columns = ['Original String', 'Modified String']

    def test_case_1(self):
        input_data = ['apple, orange, banana', 'car, bike, plane']
        result = task_func(input_data, seed=42)
        self._test_dataframe(result, input_data)

    def test_case_2(self):
        input_data = ['a, b, c, d, e', 'f, g, h, i, j']
        result = task_func(input_data, seed=42)
        self._test_dataframe(result, input_data)

    def test_case_3(self):
        input_data = ['1, 2, 3', '4, 5, 6, 7']
        result = task_func(input_data, seed=42)
        self._test_dataframe(result, input_data)

    def _test_dataframe(self, df, input_data):
        self.assertListEqual(list(df.columns), self.columns)
        for orig, mod in zip(df['Original String'], df['Modified String']):
            self.assertTrue(orig in input_data)
            self.assertEqual(len(orig.split(', ')) - 1, len(mod.split(', ')))
