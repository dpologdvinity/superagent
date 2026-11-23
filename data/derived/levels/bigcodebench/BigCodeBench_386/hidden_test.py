from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        np.random.seed(0)
        df = task_func(100, 0, 1)
        self.assertEqual(df.shape[0], 1)
        self.assertEqual(list(df.columns), ['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])
    def test_case_2(self):
        np.random.seed(0)
        min_value = 0
        max_value = 1
        length = 10
        cdf = task_func(length, min_value, max_value)
        self.assertEqual(cdf.iloc[0]['Column1'], 10)
    def test_case_3(self):
        np.random.seed(0)
        df = task_func(100)
        #self.assertEqual(df.shape[0], 100)
        self.assertEqual(list(df.columns), ['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])
    def test_case_4(self):
        np.random.seed(0)
        df = task_func(100, 50, 100)
        self.assertEqual(list(df.columns), ['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])
        for column in df.columns:
            self.assertTrue(all(df[column].diff().dropna() >= 0))
    def test_case_5(self):
        np.random.seed(0)
        df  = task_func(0)
        self.assertEqual(df.shape[0], 0)
        self.assertEqual(list(df.columns), ['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])
