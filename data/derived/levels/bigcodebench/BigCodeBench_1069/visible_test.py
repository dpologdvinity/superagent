from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):
    """Test cases for task_func function."""

    def test_uniform_distribution(self):
        """Test for uniform distribution."""
        data = {'Category1': ['A', 'A', 'B', 'B', 'C', 'C'], 'Category2': ['X', 'X', 'Y', 'Y', 'Z', 'Z']}
        axes = task_func(data)
        self.assertEqual([ax.get_title() for ax in axes], ['Category1', 'Category2'])

    def test_non_uniform_distribution(self):
        """Test for non-uniform distribution."""
        data = {'Category1': ['A', 'A', 'B', 'B', 'C', 'C', 'C'], 'Category2': ['X', 'X', 'Y', 'Y', 'Z', 'Z', 'Z']}
        axes = task_func(data)
        self.assertEqual([ax.get_title() for ax in axes], ['Category1', 'Category2'])

    def test_single_column(self):
        """Test for single column."""
        data = {'Category1': ['A', 'A', 'B', 'B', 'C', 'C']}
        axes = task_func(data)
        self.assertEqual([ax.get_title() for ax in axes], ['Category1'])
