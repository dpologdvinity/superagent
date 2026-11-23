from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_data = pd.DataFrame({'Name': ['John', 'Anna', 'Peter'], 'Age': [27, 23, 29], 'Salary': [50000, 60000, 70000], 'UnicodeString': ['John', 'Anna', 'Peter']})

    def test_unicode_decoding(self):
        decoded_df = task_func(self.test_data)
        expected_strings = ['John', 'Anna', 'Peter']
        self.assertListEqual(list(decoded_df['UnicodeString']), expected_strings)

    def test_missing_column(self):
        with self.assertRaises(KeyError):
            task_func(pd.DataFrame({'Name': ['John']}))

    def test_non_dataframe_input(self):
        with self.assertRaises(TypeError):
            task_func('Not a DataFrame')
