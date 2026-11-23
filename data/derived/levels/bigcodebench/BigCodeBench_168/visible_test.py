from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')

class TestCases(unittest.TestCase):

    def tearDown(self):
        """Ensure no files are left after tests."""
        try:
            os.remove('test_plot.png')
        except FileNotFoundError:
            pass

    def test_default_parameters(self):
        """Test the function with default parameters."""
        fig, data, plot_filename = task_func()
        self.assertIsInstance(fig, plt.Figure, 'The function should return a matplotlib.figure.Figure object.')
        self.assertEqual(data.shape, (5, 5), 'The default DataFrame should have 5 rows and 5 columns.')
        expected_columns = ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
        self.assertListEqual(list(data.columns), expected_columns, 'Default column labels are incorrect.')
        self.assertTrue(os.path.exists(plot_filename), 'Plot file should be created.')

    def test_custom_parameters(self):
        """Test the function with custom number of groups, data size, and labels."""
        num_groups, data_size, labels = (3, 4, ['A', 'B', 'C'])
        fig, data, plot_filename = task_func(num_groups=num_groups, data_size=data_size, labels=labels)
        self.assertIsInstance(fig, plt.Figure, 'The function should return a matplotlib.figure.Figure object.')
        self.assertEqual(data.shape, (4, 3), 'DataFrame dimensions should match the custom parameters.')
        self.assertListEqual(list(data.columns), labels, 'Column labels should match the custom labels provided.')

    def test_data_values(self):
        """Test that the data in the DataFrame is within the expected range (0.0, 1.0)."""
        fig, data, plot_filename = task_func()
        self.assertTrue((data >= 0.0).all().all() and (data <= 1.0).all().all(), 'All data should be within the range [0.0, 1.0].')
