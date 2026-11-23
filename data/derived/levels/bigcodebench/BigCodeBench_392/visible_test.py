from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker
faker = Faker()
COLORS = ['r', 'g', 'b']

class TestCases(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'Group': ['A', 'B', 'C'], 'Value': [10, 20, 30]})

    def test_single_group_bar_chart(self):
        ax = task_func(self.df, 'Group', 'Value', 'B')
        num_bars = len(ax.containers[0])
        self.assertEqual(num_bars, 1)
        plt.close()

    def test_missing_group(self):
        with self.assertRaises(ValueError):
            ax = task_func(self.df, 'Group', 'Value', 'D')
        plt.close()

    def test_correct_labels(self):
        ax = task_func(self.df, 'Group', 'Value', 'B')
        self.assertEqual(ax.get_xlabel(), 'Group')
        self.assertEqual(ax.get_ylabel(), 'Value')
        plt.close()

def generate_complex_test_data(num_rows=100):
    """Generate a DataFrame with a mix of numeric and text data, including some potential outliers."""
    data = {'Group': [faker.random_element(elements=('A', 'B', 'C', 'D')) for _ in range(num_rows)], 'Value': [faker.random_int(min=0, max=1000) for _ in range(num_rows)]}
    complex_df = pd.DataFrame(data)
    return complex_df
