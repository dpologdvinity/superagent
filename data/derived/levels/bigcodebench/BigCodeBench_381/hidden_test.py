from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import os
import numpy as np
from numpy.testing import assert_array_almost_equal
def create_dummy_file(file_path):
    data = {
        'Index': [1, 2, 3],
        'Score1': [10, 15, 20],
        'Score2': [20, 25, 30],
        'Score3': [30, 35, 40]
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
class TestCases(unittest.TestCase):    
    def setUp(self):
        # Create a dummy CSV for testing
        data = {
            'Index': [1, 2, 3],
            'Score1': [10, 15, 20],
            'Score2': [20, 25, 30],
            'Score3': [30, 35, 40]
        }
        df = pd.DataFrame(data)
        df.to_csv('dummy_arena.csv', index=False)
        
        # Create a more complex dummy CSV for advanced testing
        np.random.seed(42)  # For reproducibility
        complex_data = {
            'Index': np.arange(1, 11),
            'Feature1': np.random.randint(-10, 50, 10),
            'Feature2': np.random.normal(0, 5, 10),
            'Feature3': np.random.uniform(25, 75, 10),
            'Feature4': np.random.lognormal(0, 1, 10),
            'Feature5': np.linspace(10, 100, 10),
            'Outcome': np.random.choice([0, 1], 10)  # Binary outcome for classification
        }
        complex_df = pd.DataFrame(complex_data)
        # Introduce some missing values
        complex_df.loc[4:6, 'Feature2'] = np.nan
        complex_df.loc[2:3, 'Feature4'] = np.nan
        complex_df.to_csv('complex_dummy_arena.csv', index=False)
    def tearDown(self):
        os.remove('dummy_arena.csv')
        os.remove('complex_dummy_arena.csv')
    def test_feature_importances(self):
        # Test the function for normal functionality
        ax, importances = task_func('dummy_arena.csv', 'Index')
        self.assertEqual(len(importances), 3)  # Expecting 3 features
        self.assertTrue(np.all(importances >= 0))  # Importances should be non-negative
        expect = np.array([0.35294118, 0.36470588, 0.28235294])
        assert_array_almost_equal(importances, expect, decimal=6)
        
    def test_file_not_found(self):
        # Test FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent.csv', 'Index')
    def test_invalid_target_column(self):
        # Test ValueError for invalid target column
        with self.assertRaises(ValueError):
            task_func('dummy_arena.csv', 'NonexistentColumn')
            
    
    def test_feature_importances1(self):
        # Test the function for normal functionality
        ax, importances = task_func('complex_dummy_arena.csv', 'Index')
        print(importances)
        expect = np.array([0.16335979, 0.22973545, 0.15900794, 0.18597884, 0.19796296, 0.06395503])
        assert_array_almost_equal(importances, expect, decimal=6)
