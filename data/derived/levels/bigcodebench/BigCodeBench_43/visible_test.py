from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):
    """Test cases for the f_112 function."""

    def setUp(self):
        self.df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15]})
        self.df2 = pd.DataFrame({'X': [1, None, 9, 13], 'Y': [None, 3, 4, 8]})
        self.df3 = pd.DataFrame({'M': [7, 13, 21, 11, 22, 8, None, 17], 'N': [None, 2, 3, 4, 10, 0, 27, 12]})
        self.df4 = pd.DataFrame({'P': [None, None, 4], 'Q': [7, None, 3], 'R': [2, None, 6]})
        self.df5 = pd.DataFrame({'W': [1, 2], 'Z': [2, 1]})
        self.df6 = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [None, 8, 9, 10, 11, None], 'C': [13, None, None, None, None, 18], 'D': [19, None, 21, None, 23, None]})

    def test_case_1(self):
        description, plots = task_func(self.df1)
        self.assertFalse(description.isna().any().any())
        self.assertIsInstance(description, pd.DataFrame)
        self.assertListEqual(list(description.columns), ['A', 'B', 'C'])
        self.assertEqual(len(plots), 3)

    def test_case_2(self):
        description, plots = task_func(self.df2)
        self.assertFalse(description.isna().any().any())
        self.assertIsInstance(description, pd.DataFrame)
        self.assertListEqual(list(description.columns), ['X', 'Y'])
        self.assertEqual(len(plots), 2)

    def test_case_3(self):
        description, plots = task_func(self.df3)
        self.assertFalse(description.isna().any().any())
        self.assertIsInstance(description, pd.DataFrame)
        self.assertListEqual(list(description.columns), ['M', 'N'])
        self.assertEqual(len(plots), 2)
