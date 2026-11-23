from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = task_func()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.iloc[:, 0].tolist(), [49, 53, 33])
        self.assertEqual(df.iloc[:, 1].tolist(), [97, 5, 65])
        
    def test_case_2(self):
        df = task_func(rows=5, cols=4)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.iloc[:, 0].tolist(), [49, 33, 38, 27, 17])
        self.assertEqual(df.iloc[:, 1].tolist(), [97, 65, 61, 64, 96])
        self.assertEqual(df.iloc[:, 2].tolist(), [53, 62, 45, 17, 12])
    def test_case_3(self):
        df = task_func(min_val=10, max_val=20)
        self.assertEqual(df.iloc[:, 0].tolist(), [16, 10, 18])
        self.assertEqual(df.iloc[:, 1].tolist(), [16, 14, 17])
        
    def test_case_4(self):
        df = task_func(min_val=50, max_val=50)
        self.assertEqual(df.iloc[:, 0].tolist(), [50, 50, 50])
        self.assertEqual(df.iloc[:, 1].tolist(), [50, 50, 50])
    def test_case_5(self):
        df = task_func(rows=0, cols=2)
        self.assertTrue(df.empty)
