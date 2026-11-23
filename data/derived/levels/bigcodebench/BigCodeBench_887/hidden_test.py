from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_rng(self):
        T1 = (('13', '17', '18', '21', '32'))
        df1 = task_func(T1, row_num=50, seed=2022)
        df2 = task_func(T1, row_num=50, seed=2022)
        pd.testing.assert_frame_equal(df1, df2)
        df4 = task_func(T1, row_num=50, seed=12)
        try:
            pd.testing.assert_frame_equal(df1, df4)
        except AssertionError:
            pass
        else:
            raise AssertionError('frames are equal but should not be')
    def test_case_1(self):
        T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
        df = task_func(T1, row_num=50, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, sum([13, 17, 18, 21, 32, 7, 11, 13, 14, 28, 1, 5, 6, 8, 15, 16])))
    def test_case_2(self):
        T1 = (('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'))
        df = task_func(T1, row_num=50, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, sum([1, 2, 3, 4, 5, 6, 7, 8, 9])))
    def test_case_3(self):
        T1 = (('10', '20', '30'), ('40', '50', '60'), ('70', '80', '90'))
        df = task_func(T1, row_num=70, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (70, sum([10, 20, 30, 40, 50, 60, 70, 80, 90])))
    def test_case_4(self):
        T1 = ()
        df = task_func(T1, row_num=50, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, 0))
    def test_case_5(self):
        T1 = (('1', '2', '3'), (), ('7', '8', '9'))
        df = task_func(T1, row_num=50, seed=21)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, sum([1, 2, 3, 7, 8, 9])))
    def test_non_int(self):
        a = (('1', '2.45'))
        self.assertRaises(Exception, task_func, a, 120, 21)
