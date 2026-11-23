from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df = task_func()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 27)

    def test_case_2(self):
        df = task_func(['X', 'Y'], ['Cat 1'])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 2)

    def test_case_3(self):
        df = task_func(['X', 'Y'], [])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 0)
