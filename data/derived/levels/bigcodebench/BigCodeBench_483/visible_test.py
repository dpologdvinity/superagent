from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'A': ['blue car red', 'green apple yellow'], 'B': [3, 4]})

    def test_case_1(self):
        df = pd.DataFrame({'Text': ['apple orange', 'blue red'], 'Number': [1, 2]})
        pattern = '\\b(?:banana|green)\\b'
        expected = df.copy()
        result = task_func(df, 'Text', pattern)
        pd.testing.assert_frame_equal(expected, result)

    def test_case_2(self):
        df = pd.DataFrame({'Text': ['apple banana', 'banana apple'], 'Number': [1, 2]})
        pattern = '\\b(?:apple|banana)\\b'
        expected = pd.DataFrame({'Text': ['banana apple', 'apple banana'], 'Number': [1, 2]})
        result = task_func(df, 'Text', pattern)
        pd.testing.assert_frame_equal(expected, result)

    def test_case_3(self):
        df = pd.DataFrame({'Text': ['apple orange banana', 'blue apple green'], 'Number': [1, 2]})
        pattern = '\\b(?:apple|banana)\\b'
        expected = pd.DataFrame({'Text': ['banana orange apple', 'blue apple green'], 'Number': [1, 2]})
        result = task_func(df, 'Text', pattern)
        pd.testing.assert_frame_equal(expected, result)
