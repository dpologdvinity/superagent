from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def setUp(self):
        self.data_dict = {'A': [10, 20, 30, 40], 'B': [20, 30, 40, 50], 'C': [30, 40, 50, 60]}

    def test_normalization_single_key(self):
        data_keys = ['A']
        normalized_df, ax = task_func(self.data_dict, data_keys)
        self.assertTrue((normalized_df >= 0).all().all() and (normalized_df <= 1).all().all(), 'Normalized data should be in the range [0, 1]')

    def test_normalization_multiple_keys(self):
        data_keys = ['A', 'B']
        normalized_df, ax = task_func(self.data_dict, data_keys)
        self.assertEqual(len(normalized_df.columns), 2, 'Normalized DataFrame should have 2 columns')
        self.assertTrue({'A', 'B'}.issubset(normalized_df.columns), 'DataFrame should contain specified keys')

    def test_normalization_all_keys(self):
        data_keys = list(self.data_dict.keys())
        normalized_df, ax = task_func(self.data_dict, data_keys)
        self.assertEqual(len(normalized_df.columns), 3, 'Normalized DataFrame should have 3 columns')
        self.assertTrue({'A', 'B', 'C'}.issubset(normalized_df.columns), 'DataFrame should contain all keys')
