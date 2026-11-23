from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import itertools
import string
import matplotlib.pyplot as plt
LETTERS = list(string.ascii_lowercase)
class TestCases(unittest.TestCase):
    """Tests for the function task_func"""
    def test_dataframe_shape(self):
        """
        Test if the DataFrame has the correct shape (17576 rows, 3 columns)
        """
        df, _ = task_func()
        self.assertEqual(df.shape, (17576, 3))
    def test_dataframe_columns(self):
        """
        Test if the DataFrame has the correct column names (a, b, c)
        """
        df, _ = task_func()
        self.assertListEqual(list(df.columns), ["a", "b", "c"])
    def test_histogram_plot(self):
        """
        Test if the histogram plot is an instance of matplotlib Axes
        """
        _, ax = task_func()
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_first_column_values(self):
        """
        Test if the first column of the DataFrame contains only lowercase letters
        """
        df, _ = task_func()
        self.assertTrue(all(letter in string.ascii_lowercase for letter in df["a"]))
    def test_no_empty_values(self):
        """
        Test if there are no empty values in the DataFrame
        """
        df, _ = task_func()
        self.assertFalse(df.isnull().values.any())
    def tearDown(self):
        plt.close()
