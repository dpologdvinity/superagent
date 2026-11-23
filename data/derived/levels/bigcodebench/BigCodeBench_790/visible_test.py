from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from faker import Faker
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        fake = Faker()
        self.df1 = pd.DataFrame({'col1': [fake.random_int(min=10, max=100) for _ in range(10)], 'col2': [fake.random_int(min=10, max=100) for _ in range(10)]})
        self.df2 = pd.DataFrame({'col1': [fake.random_int(min=-100, max=-10) for _ in range(10)], 'col2': [fake.random_int(min=10, max=100) for _ in range(10)]})
        self.df3 = pd.DataFrame({'col1': [fake.random_int(min=-100, max=100) for _ in range(10)], 'col2': [fake.random_int(min=-100, max=100) for _ in range(10)]})
        self.df4 = pd.DataFrame({'col1': [fake.random_int(min=0, max=10) for _ in range(10)], 'col2': [fake.random_int(min=90, max=100) for _ in range(10)]})
        self.df5 = pd.DataFrame({'col1': [fake.random_int(min=10, max=20) for _ in range(10)], 'col2': [fake.random_int(min=10, max=20) for _ in range(10)]})

    def test_wrong_columns(self):
        data = {'col1': [1, 2, 3, 4, 5], 'col2': [2, 3, 4, 5, 6]}
        df = pd.DataFrame(data)
        self.assertRaises(Exception, task_func, df, 'a', 'col2')
        self.assertRaises(Exception, task_func, df, 'col1', 'a')
        self.assertRaises(Exception, task_func, df, 'a', 'b')

    def test_case_1(self):
        result = task_func(self.df1, 'col1', 'col2')
        self.assertTrue(isinstance(result, list))
        self.assertEqual(len(result), 10)

    def test_case_2(self):
        result = task_func(self.df2, 'col1', 'col2', 5)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(len(result), 5)
