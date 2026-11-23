from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):
    """Unit tests for the function."""

    def test_empty_data(self):
        """
        Test with an empty dictionary. Should return an empty DataFrame and a plot object.
        """
        result_df, result_ax = task_func({})
        self.assertTrue(result_df.empty)
        self.assertIsNotNone(result_ax)

    def test_all_none_data(self):
        """
        Test with a dictionary where all values are None. Should return an empty DataFrame and a plot object.
        """
        data = {'a': [None, None], 'b': [None, None]}
        result_df, result_ax = task_func(data)
        self.assertTrue(result_df.empty)
        self.assertIsNotNone(result_ax)

    def test_normal_data(self):
        """
        Test with a normal data dictionary. Should return a non-empty DataFrame and a plot object.
        """
        data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
        result_df, result_ax = task_func(data)
        self.assertEqual(result_ax.get_title(), 'Scaled Values')
        self.assertFalse(result_df.empty)
        self.assertEqual(result_df.shape, (3, 2))
        self.assertIsNotNone(result_ax)
