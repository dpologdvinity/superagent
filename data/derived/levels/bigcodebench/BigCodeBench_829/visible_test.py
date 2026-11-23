from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from statistics import mean
from faker import Faker
fake = Faker()

class TestCases(unittest.TestCase):

    def test_case_wrong_columns(self):
        df_sample1 = pd.DataFrame({'A': ['Tom', 'Nick', 'John', 'Tom', 'John'], 'Score': [85, 79, 90, 88, 82]})
        self.assertRaises(Exception, task_func, df_sample1)

    def test_case_1(self):
        df_test = pd.DataFrame({'Name': ['Tom', 'Nick', 'John'], 'Score': [85, 79, 90]})
        gen_dict = task_func(df_test)
        expected_result = {'John': ('John', 90), 'Nick': ('Nick', 79), 'Tom': ('Tom', 85)}
        self.assertDictEqual({key: next(value) for key, value in gen_dict.items()}, expected_result)

    def test_case_2(self):
        df_test = pd.DataFrame({'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'], 'Score': [85, 79, 90, 88, 82]})
        gen_dict = task_func(df_test)
        expected_result = {'John': ('John', 86), 'Nick': ('Nick', 79), 'Tom': ('Tom', 86.5)}
        self.assertDictEqual({key: next(value) for key, value in gen_dict.items()}, expected_result)
