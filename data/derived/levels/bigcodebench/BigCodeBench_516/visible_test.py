from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_case_1(self):
        test_data = [([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 42, 1.0), ([[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10]], 42, 1.0), ([[100, 200, 300, 400, 500], [600, 700, 800, 900, 1000]], 42, 1.0)]
        for array, random_seed, expected_r2 in test_data:
            with self.subTest(array=array):
                df, results = task_func(array, random_seed=random_seed)
                expected_df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'Response'])
                self.assertTrue(df.equals(expected_df))
                self.assertAlmostEqual(results.rsquared, expected_r2, places=2)
                for param in results.params:
                    self.assertNotEqual(param, 0)

    def test_case_2(self):
        random_seed = 42
        array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
        df, results = task_func(array, random_seed=random_seed)
        expected_df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'Response'])
        self.assertTrue(df.equals(expected_df))
        self.assertAlmostEqual(results.rsquared, 1.0, places=2)
        for param in results.params:
            self.assertNotEqual(param, 0)

    def test_case_3(self):
        array = [[1, 2, 3, 4], [5, 6, 7, 8]]
        with self.assertRaises(ValueError):
            task_func(array)
