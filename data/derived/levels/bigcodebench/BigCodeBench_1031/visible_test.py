from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random
from matplotlib.axes import Axes
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    """Tests for the function task_func."""

    def test_return_type(self):
        """Test if the function returns a Matplotlib Axes object."""
        random.seed(0)
        result = task_func(100)
        self.assertIsInstance(result, Axes)

    def test_default_parameter(self):
        """Test the function with the default parameter."""
        result = task_func()
        self.assertIsInstance(result, Axes)

    def test_zero_rows(self):
        """Test the function with zero rows."""
        with self.assertRaises(ValueError):
            task_func(0)

    def tearDown(self):
        plt.close()
