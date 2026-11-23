from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing dataframe creation, model accuracy, and parameters with various numeric data types
        test_data = [
            ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 42, 1.0),  # Positive values
            ([[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10]], 42, 1.0),  # Negative values
            (
                [[100, 200, 300, 400, 500], [600, 700, 800, 900, 1000]],
                42,
                1.0,
            ),  # Large values
        ]
        for array, random_seed, expected_r2 in test_data:
            with self.subTest(array=array):
                df, results = task_func(array, random_seed=random_seed)
                expected_df = pd.DataFrame(
                    array, columns=["A", "B", "C", "D", "Response"]
                )
                self.assertTrue(df.equals(expected_df))
                self.assertAlmostEqual(results.rsquared, expected_r2, places=2)
                for param in results.params:
                    self.assertNotEqual(param, 0)
    def test_case_2(self):
        # Testing with more rows in the 2D list to ensure model scalability and consistency
        random_seed = 42
        array = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ]
        df, results = task_func(array, random_seed=random_seed)
        expected_df = pd.DataFrame(array, columns=["A", "B", "C", "D", "Response"])
        self.assertTrue(df.equals(expected_df))
        self.assertAlmostEqual(results.rsquared, 1.0, places=2)
        for param in results.params:
            self.assertNotEqual(param, 0)
    def test_case_3(self):
        # Testing input validation for incorrect number of columns in a row
        array = [[1, 2, 3, 4], [5, 6, 7, 8]]  # Missing dependent variable
        with self.assertRaises(ValueError):
            task_func(array)
    def test_case_4(self):
        # Testing handling of non-numeric values to ensure type safety
        array = [["a", "b", "c", "d", "e"]]  # All elements as strings
        with self.assertRaises(ValueError):
            df, results = task_func(array)
            # This assumes the function is modified to catch and raise ValueError for non-numeric inputs
    def test_case_5(self):
        # Testing reproducibility by using the same random_seed
        array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        random_seed = 123
        df1, results1 = task_func(array, random_seed=random_seed)
        df2, results2 = task_func(array, random_seed=random_seed)
        self.assertTrue(df1.equals(df2))
        self.assertEqual(results1.params.tolist(), results2.params.tolist())
    def test_case_6(self):
        # Testing with an empty array to check function's handling of no input data
        array = []
        with self.assertRaises(ValueError):
            task_func(array)
