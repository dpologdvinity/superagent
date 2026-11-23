from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import matplotlib.pyplot as plt
import pandas as pd
# Check and set the backend
class TestCases(unittest.TestCase):
    def setUp(self):
        self.words = ['apple', 'banana', 'cherry', 'date', 'apricot', 'blueberry', 'avocado']
        self.df = pd.DataFrame({'Word': self.words})
    @patch('seaborn.boxplot')
    def test_word_filtering(self, mock_boxplot):
        """Test if the function correctly filters words starting with a given letter."""
        task_func(self.df, 'a')
        filtered_words = ['apple', 'apricot', 'avocado']
        self.assertTrue(all(word.startswith('a') for word in filtered_words), "Word filtering by letter 'a' failed.")
    @patch('seaborn.boxplot')
    def test_boxplot_called(self, mock_boxplot):
        """Test if seaborn's boxplot is called when valid data is provided."""
        task_func(self.df, 'a')
        mock_boxplot.assert_called_once()
    @patch('matplotlib.pyplot.show')
    def test_return_type(self, mock_show):
        """Test the return type is an Axes."""
        ax = task_func(self.df, 'a')
        self.assertIsInstance(ax, plt.Axes)
    def test_empty_dataframe(self):
        """Test handling of empty DataFrame."""
        empty_df = pd.DataFrame({'Word': []})
        result = task_func(empty_df, 'a')
        self.assertIsNone(result, "Empty DataFrame should return None.")
    def test_no_word_column(self):
        """Test handling of DataFrame without 'Word' column."""
        df_without_word = pd.DataFrame({'NoWord': self.words})
        with self.assertRaises(ValueError):
            task_func(df_without_word, 'a')
