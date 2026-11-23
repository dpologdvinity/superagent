from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        """Initialize testing dataframe."""
        self.df = {'Word': ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'avocado']}
    @patch('matplotlib.pyplot.hist')
    def test_filter_by_letter(self, mock_hist):
        """Test filtering functionality by a specific letter."""
        task_func(self.df, 'a')
        filtered_words = ['apple', 'avocado']
        self.assertTrue(all(word in self.df['Word'] for word in filtered_words))
    @patch('matplotlib.pyplot.hist')
    def test_return_type(self, mock_hist):
        """Test the return type is a matplotlib Axes."""
        ax = task_func(self.df, 'a')
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_histogram_plot_calls(self):
        """Test if histogram plot is generated with correct parameters."""
        with patch('pandas.Series.hist') as mock_hist:
            task_func(self.df, 'd')
            mock_hist.assert_called_once()
    def test_word_length_calculation(self):
        """Test if word lengths are calculated correctly for words starting with 'a'."""
        ax = task_func(self.df, 'a')
        expected_lengths = [5, 7]  # Lengths of 'apple' and 'avocado'
        filtered_words = [word for word in self.df['Word'] if word.startswith('a')]
        actual_lengths = [len(word) for word in filtered_words]
        # Test if actual lengths match expected lengths
        self.assertEqual(expected_lengths, actual_lengths, "The word lengths do not match expected results.")
    @patch('matplotlib.pyplot.hist')
    def test_nonexistent_letter(self, mock_hist):
        """Test filtering by a letter not present returns None."""
        ax = task_func(self.df, 'z')
        self.assertIsNone(ax, "Expected None when no words start with the specified letter.")
