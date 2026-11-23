from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)  # Set a seed for reproducibility
    def test_case_1(self):
        # Test with a DataFrame of random values
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper) 
        self.assertEqual(results.params.index.to_list(), ['const', 'Height', 'Weight']) # There should be 3 parameters: const, Height, Weight
    def test_case_2(self):
        # Test with a DataFrame where no rows match the condition
        df = pd.DataFrame(np.random.randint(30,40,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsNone(results) # There should be no regression result since no rows match the condition
    def test_case_3(self):
        # Test with a DataFrame where all rows match the condition
        df = pd.DataFrame(np.random.randint(60,80,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper) 
        self.assertEqual(results.params.index.to_list(), ['const', 'Height', 'Weight']) # There should be 3 parameters: const, Height, Weight
    def test_case_4(self):
        # Test with a DataFrame with different column names
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 3)), columns=['Years', 'Size', 'Mass'])
        results = task_func(df, 50, 70, columns=['Years', 'Size', 'Mass'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper) 
        self.assertEqual(results.params.index.to_list(), ['const', 'Size', 'Mass']) # There should be 3 parameters: const, Height, Weight
    def test_case_5(self):
        # Test with an empty DataFrame
        df = pd.DataFrame(columns=['Age', 'Height', 'Weight'])
        results = task_func(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsNone(results) # There should be no regression result since DataFrame is empty
