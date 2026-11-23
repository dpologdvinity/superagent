from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        df, distance_matrix = task_func(input_data)
        self.assertEqual(df.shape, (2, 5))
        self.assertTrue((df.columns == ['A', 'B', 'C', 'D', 'E']).all())
        self.assertEqual(distance_matrix.shape, (2, 2))
        self.assertAlmostEqual(distance_matrix.iloc[0, 1], 11.18034, places=5)
        self.assertAlmostEqual(distance_matrix.iloc[1, 0], 11.18034, places=5)

    def test_case_2(self):
        input_data = [[-5, -4, -3, -2, -1], [0, 0, 0, 0, 0], [1, 2, 3, 4, 5]]
        df, distance_matrix = task_func(input_data)
        self.assertEqual(df.shape, (3, 5))
        self.assertEqual(distance_matrix.shape, (3, 3))
        self.assertAlmostEqual(distance_matrix.iloc[0, 1], 7.4162, places=5)
        self.assertAlmostEqual(distance_matrix.iloc[1, 2], 7.4162, places=5)

    def test_case_3(self):
        input_data = [[1, 2], [3, 4]]
        df, distance_matrix = task_func(input_data)
        self.assertEqual(df.shape, (2, 2))
        self.assertEqual(distance_matrix.shape, (2, 2))
        self.assertAlmostEqual(distance_matrix.iloc[0, 1], 2.82843, places=5)
