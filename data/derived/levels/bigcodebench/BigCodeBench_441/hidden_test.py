from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        self.test_P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.test_T = np.random.rand(3, 3, 3)
    def check_result_correctness(self, P, T, result):
        # Manually compute the expected result for the matrix-tensor product
        expected_result = np.einsum("ij,jkl->ik", P, T)
        return np.allclose(result, expected_result)
    def test_case_1(self):
        # Test output visualization
        _, ax = task_func(self.test_P, self.test_T)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        # Test result correctness
        result, _ = task_func(self.test_P, self.test_T)
        self.assertTrue(self.check_result_correctness(self.test_P, self.test_T, result))
        self.assertEqual(result.shape, (self.test_P.shape[0], 3))
    def test_case_3(self):
        # Test with zeros and negative values
        P = np.array([[0, 0, 0]])
        T = np.random.rand(3, 3, 3) - 0.5
        result, _ = task_func(P, T)
        self.assertTrue(np.all(result == 0))
    def test_case_4(self):
        # Test with non-numeric data
        P = np.array([["a", "b", "c"], [1, 2, 3]])
        with self.assertRaises(Exception):
            task_func(P, self.test_T)
    def test_case_5(self):
        # Test incompatible shapes
        P = np.array([[1, 2], [3, 4]])
        with self.assertRaises(Exception):
            task_func(P, self.test_T)
    def test_case_6(self):
        # Test incompatible input types
        with self.assertRaises(Exception):
            task_func([1, 2], [2, 1])
    def tearDown(self):
        plt.close("all")
