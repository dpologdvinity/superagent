from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        df_standardized = task_func(df)
        self.assertAlmostEqual(df_standardized['a'].mean(), 0)
        self.assertAlmostEqual(df_standardized['a'].std(), 1.224744871391589)
    def test_case_2(self):
        df = pd.DataFrame({'a': [1, 1, 1], 'b': [1, 1, 1]})
        df_standardized = task_func(df)
        self.assertAlmostEqual(df_standardized['a'].mean(), 0)
        self.assertAlmostEqual(df_standardized['a'].std(), 0)
    def test_case_3(self):
        df = pd.DataFrame({'a': [1, 0, -1], 'b': [0, 1, 0]})
        df_standardized = task_func(df)
        print(df_standardized)
        self.assertAlmostEqual(df_standardized['a'].mean(), 0)
        self.assertAlmostEqual(df_standardized['a'].std(), 1.224744871391589)
    def test_case_4(self):
        df = pd.DataFrame({'z': [1, 2, 3], 'y': [4, 5, 6]})
        df_standardized = task_func(df)
        self.assertAlmostEqual(df_standardized['z'].mean(), 0)
        self.assertAlmostEqual(df_standardized['z'].std(), 1.224744871391589)
    def test_case_5(self):
        df = pd.DataFrame({'z': [1, 2, 3], 'y': [4, 5, 6]})
        df_standardized = task_func(df)
        self.assertAlmostEqual(df_standardized['y'].mean(), 0)
        self.assertAlmostEqual(df_standardized['y'].std(), 1.224744871391589)
