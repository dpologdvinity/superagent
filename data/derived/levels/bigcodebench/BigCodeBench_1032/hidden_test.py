from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
import random
class TestCases(unittest.TestCase):
    """Tests for task_func."""
    def test_default_parameters(self):
        """
        Test task_func with default parameters (rows=1000, string_length=3).
        Verifies if the function returns a matplotlib Axes object.
        """
        random.seed(0)
        result = task_func()
        self.assertIsInstance(result, plt.Axes)
    def test_custom_rows(self):
        """
        Test task_func with a custom number of rows.
        Verifies if the function still returns a matplotlib Axes object.
        """
        random.seed(1)
        result = task_func(rows=500)
        self.assertIsInstance(result, plt.Axes)
    def test_custom_string_length(self):
        """
        Test task_func with a custom string length.
        Verifies if the function still returns a matplotlib Axes object.
        """
        random.seed(2)
        result = task_func(string_length=5)
        self.assertIsInstance(result, plt.Axes)
    def test_large_dataset(self):
        """
        Test task_func with a large dataset.
        Verifies if the function can handle a large number of rows without errors.
        """
        random.seed(3)
        result = task_func(rows=10000, string_length=3)
        self.assertIsInstance(result, plt.Axes)
    def test_zero_rows(self):
        """
        Test task_func with zero rows.
        Verifies if the function handles edge case of zero rows by returning None.
        """
        random.seed(4)
        result = task_func(rows=0)
        self.assertIsNone(result, "Function should return None for zero rows.")
    def tearDown(self):
        plt.close()
