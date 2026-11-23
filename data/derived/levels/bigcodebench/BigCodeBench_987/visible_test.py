from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_data_extraction(self):
        json_str = '{"data": {"values": [0.5, 10, 15, 20]}}'
        data_key = 'data.values'
        original_data, _, _ = task_func(json_str, data_key)
        expected_series = pd.Series([0.5, 10, 15, 20], dtype=pd.Float64Dtype)
        pd.testing.assert_series_equal(original_data, expected_series, check_dtype=False)

    def test_data_normalization(self):
        json_str = '{"data": {"values": [0, 10, 20, 30, 40]}}'
        data_key = 'data.values'
        _, normalized_data, _ = task_func(json_str, data_key)
        expected_normalized = pd.Series([0.0, 0.25, 0.5, 0.75, 1.0], dtype=pd.Float64Dtype)
        pd.testing.assert_series_equal(normalized_data, expected_normalized, check_dtype=False)

    def test_plot_properties(self):
        json_str = '{"data": {"values": [1, 2, 3, 4, 5]}}'
        data_key = 'data.values'
        _, _, ax = task_func(json_str, data_key)
        self.assertEqual(ax.get_title(), 'Comparison of Original and Normalized Data')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Value')
        legend_texts = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertIn('Original Data', legend_texts)
        self.assertIn('Normalized Data', legend_texts)
