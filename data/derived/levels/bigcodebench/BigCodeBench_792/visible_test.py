from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from faker import Faker
import pandas as pd
fake = Faker()

class TestCases(unittest.TestCase):

    def setUp(self):
        self.sample_data = {'col1': [fake.random_int(min=1, max=100) for _ in range(100)], 'col2': [fake.random_int(min=1, max=100) for _ in range(100)]}

    def test_wrong_columns(self):
        data = {'col1': [1, 2, 3, 4, 5], 'col2': [2, 3, 4, 5, 6]}
        df = pd.DataFrame(data)
        self.assertRaises(Exception, task_func, df, 'a', 'col2')
        self.assertRaises(Exception, task_func, df, 'col1', 'a')
        self.assertRaises(Exception, task_func, df, 'a', 'b')

    def test_case_1(self):
        indices, model = task_func(pd.DataFrame(self.sample_data), 'col1', 'col2')
        self.assertTrue(isinstance(model, LinearRegression))
        self.assertEqual(len(indices), 10)

    def test_case_2(self):
        indices, model = task_func(pd.DataFrame(self.sample_data), 'col1', 'col2', n=5)
        self.assertTrue(isinstance(model, LinearRegression))
        self.assertEqual(len(indices), 5)
