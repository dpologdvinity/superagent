from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from faker import Faker
import numpy as np

class TestCases(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()

    def generate_test_dataframe(self, num_rows):
        data = {'id': [self.fake.random_int(min=1, max=5) for _ in range(num_rows)], 'age': [self.fake.random_int(min=18, max=80) for _ in range(num_rows)], 'income': [self.fake.random_int(min=20000, max=100000) for _ in range(num_rows)]}
        return pd.DataFrame(data)

    def test_empty_dataframe(self):
        df = pd.DataFrame()
        with self.assertRaises(Exception):
            scaled_df, income_hist = task_func(df)

    def test_single_group_dataframe(self):
        df = self.generate_test_dataframe(1)
        scaled_df, income_hist = task_func(df)
        self.assertEqual(len(scaled_df), 1)
        self.assertEqual(len(income_hist[0]), 10)

    def test_multiple_groups_dataframe(self):
        df = self.generate_test_dataframe(100)
        scaled_df, income_hist = task_func(df)
        self.assertEqual(len(scaled_df), 100)
        self.assertEqual(len(income_hist[0]), 10)
