from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import pandas as pd 
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        self.df = pd.DataFrame({
            'A': np.random.normal(0, 1, 1000), 
            'B': np.random.exponential(1, 1000), 
            'C': np.random.randint(0, 100, 1000)
        })
    def test_standardized_columns(self):
        standardized_df = task_func(self.df, ['A', 'B'])
        self.assertAlmostEqual(standardized_df['A'].mean(), 0, places=1)
        self.assertAlmostEqual(standardized_df['A'].std(), 1, places=1)
        self.assertAlmostEqual(standardized_df['B'].mean(), 0, places=1)
        self.assertAlmostEqual(standardized_df['B'].std(), 1, places=1)
        df_list = standardized_df.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        with open('df_contents.txt', 'w') as file:
            file.write(str(df_list))
    def test_invalid_input_dataframe(self):
        with self.assertRaises(ValueError):
            task_func("not a dataframe", ['A', 'B'])
    def test_invalid_input_cols(self):
        with self.assertRaises(ValueError):
            task_func(self.df, 'A')
    def test_nonexistent_column(self):
        with self.assertRaises(ValueError):
            task_func(self.df, ['A', 'NonexistentColumn'])
    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame(), ['A', 'B'])
