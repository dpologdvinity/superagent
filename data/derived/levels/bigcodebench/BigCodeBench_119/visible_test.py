from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch, ANY

class TestCases(unittest.TestCase):

    def test_no_error(self):
        """Test that the function runs without error."""
        try:
            task_func()
        except Exception as e:
            self.fail(f'Function task_func raised an exception: {e}')

    def test_plot_elements(self):
        """Test that the plot contains correct elements like title and labels."""
        with patch('matplotlib.pyplot.show'):
            task_func()
            fig = plt.gcf()
            self.assertEqual(fig.axes[0].get_title(), 'y = x^2')
            self.assertEqual(fig.axes[0].get_xlabel(), 'x')
            self.assertEqual(fig.axes[0].get_ylabel(), 'y')

    @patch('numpy.linspace')
    @patch('matplotlib.pyplot.plot')
    def test_plot_data(self, mock_plot, mock_linspace):
        """Test if the plot contains the correct data."""
        mock_linspace.return_value = np.linspace(-10, 10, 400)
        expected_X = np.linspace(-10, 10, 400)
        expected_Y = expected_X ** 2
        with patch('matplotlib.pyplot.show'):
            task_func()
            args, kwargs = mock_plot.call_args
            self.assertTrue(np.allclose(args[0], expected_X))
            self.assertTrue(np.allclose(args[1], expected_Y))
