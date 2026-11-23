from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        np.random.seed(0)

    @patch('matplotlib.pyplot.subplots')
    @patch('pandas.DataFrame.plot')
    def test_default_parameters(self, mock_plot, mock_subplots):
        """Test using default parameters."""
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        fig = task_func()
        mock_plot.assert_called_once()
        mock_plot.assert_called_with(kind='bar', stacked=True, ax=mock_ax)
        self.assertIsInstance(fig, MagicMock)

    @patch('matplotlib.pyplot.subplots')
    @patch('pandas.DataFrame.plot')
    def test_custom_parameters(self, mock_plot, mock_subplots):
        """Test with custom parameters."""
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        num_labels = 4
        data_range = (1, 10)
        fig = task_func(num_labels=num_labels, data_range=data_range)
        mock_plot.assert_called_once()
        mock_plot.assert_called_with(kind='bar', stacked=True, ax=mock_ax)
        self.assertIsInstance(fig, MagicMock)

    @patch('matplotlib.pyplot.subplots')
    @patch('pandas.DataFrame.plot')
    def test_custom_data_range(self, mock_plot, mock_subplots):
        """Test with a custom data range."""
        data_range = (10, 20)
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        fig = task_func(data_range=data_range)
        mock_plot.assert_called_once()
        mock_plot.assert_called_with(kind='bar', stacked=True, ax=mock_ax)
        self.assertIsInstance(fig, MagicMock)
