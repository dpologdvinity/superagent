from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import pandas as pd
import unittest

class TestCases(unittest.TestCase):
    """Tests for the function task_func."""

    def test_intersection_exists(self):
        """Test that the function works when the two series have an intersection."""
        s1 = pd.Series([1, 2, 3, 4, 5], name='Series1')
        s2 = pd.Series([4, 5, 6, 7, 8], name='Series2')
        ax, intersection_count = task_func(s1, s2)
        self.assertEqual(ax.get_title(), 'Overlap Between Series1 and Series2')
        self.assertEqual(intersection_count, 2)

    def test_no_intersection(self):
        """Test that the function works when the two series have no intersection."""
        s1 = pd.Series([1, 2, 3], name='Series1')
        s2 = pd.Series([4, 5, 6], name='Series2')
        ax, intersection_count = task_func(s1, s2)
        self.assertEqual(ax.get_title(), 'Overlap Between Series1 and Series2')
        self.assertEqual(intersection_count, 0)

    def test_empty_series(self):
        """Test that the function works when one of the series is empty."""
        s1 = pd.Series([], name='Series1')
        s2 = pd.Series([], name='Series2')
        ax, intersection_count = task_func(s1, s2)
        self.assertEqual(ax.get_title(), 'Overlap Between Series1 and Series2')
        self.assertEqual(intersection_count, 0)

    def tearDown(self):
        plt.clf()
