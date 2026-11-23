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
        expected_result = np.einsum('ij,jkl->ik', P, T)
        return np.allclose(result, expected_result)

    def test_case_1(self):
        _, ax = task_func(self.test_P, self.test_T)
        self.assertIsInstance(ax, plt.Axes)

    def test_case_2(self):
        result, _ = task_func(self.test_P, self.test_T)
        self.assertTrue(self.check_result_correctness(self.test_P, self.test_T, result))
        self.assertEqual(result.shape, (self.test_P.shape[0], 3))

    def test_case_3(self):
        P = np.array([[0, 0, 0]])
        T = np.random.rand(3, 3, 3) - 0.5
        result, _ = task_func(P, T)
        self.assertTrue(np.all(result == 0))

    def tearDown(self):
        plt.close('all')
