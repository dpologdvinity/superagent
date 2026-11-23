from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from faker import Faker
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setting up Faker for test data generation
        self.fake = Faker()
    def generate_test_dataframe(self, num_rows):
        # Generating a test DataFrame with 'id', 'age', and 'income' columns
        data = {
            'id': [self.fake.random_int(min=1, max=5) for _ in range(num_rows)],
            'age': [self.fake.random_int(min=18, max=80) for _ in range(num_rows)],
            'income': [self.fake.random_int(min=20000, max=100000) for _ in range(num_rows)]
        }
        return pd.DataFrame(data)
    def test_empty_dataframe(self):
        df = pd.DataFrame()
        with self.assertRaises(Exception):
            scaled_df, income_hist = task_func(df)
    def test_single_group_dataframe(self):
        df = self.generate_test_dataframe(1)
        scaled_df, income_hist = task_func(df)
        self.assertEqual(len(scaled_df), 1)  # Only one row, hence one row in scaled DataFrame
        self.assertEqual(len(income_hist[0]), 10)  # Histogram should have 10 bins by default
    def test_multiple_groups_dataframe(self):
        df = self.generate_test_dataframe(100)
        scaled_df, income_hist = task_func(df)
        self.assertEqual(len(scaled_df), 100)  # Should have the same number of rows as input DataFrame
        self.assertEqual(len(income_hist[0]), 10)  # Checking histogram bin count
    def test_scaled_values_range(self):
        df = self.generate_test_dataframe(50)
        scaled_df, _ = task_func(df)
        self.assertEqual(len(scaled_df[(0.0 > scaled_df['age']) & (scaled_df['age'] > 1.0)]), 0)  # Age should be scaled between 0 and 1
        self.assertEqual(len(scaled_df[(0.0 > scaled_df['income']) & (scaled_df['income'] > 1.0)]), 0)  # Age should be scaled between 0 and 1
        
    def test_histogram_data_integrity(self):
        df = self.generate_test_dataframe(50)
        _, income_hist = task_func(df)
        self.assertTrue(np.all(income_hist[0] >= 0))  # Histogram counts should be non-negative
        self.assertTrue(np.all(np.diff(income_hist[1]) > 0))  # Histogram bins should be in ascending order
