from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with default parameters
        df = task_func()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 27)  # 9 letters * 3 categories
    def test_case_2(self):
        # Testing with custom parameters
        df = task_func(['X', 'Y'], ['Cat 1'])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 2)  # 2 letters * 1 category
    def test_case_3(self):
        # Testing with empty categories list
        df = task_func(['X', 'Y'], [])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 0)  # 2 letters * 0 categories
    def test_case_4(self):
        # Testing with empty letters list
        df = task_func([], ['Cat 1', 'Cat 2'])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 0)  # 0 letters * 2 categories
    def test_case_5(self):
        # Testing with both empty lists
        df = task_func([], [])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 0)  # 0 letters * 0 categories
