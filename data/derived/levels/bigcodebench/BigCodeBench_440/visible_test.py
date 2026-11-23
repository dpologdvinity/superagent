from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
from sklearn.preprocessing import StandardScaler

class TestCases(unittest.TestCase):

    def tensor_product_manual(self, P, T):
        """Manually compute the tensor product without any normalization."""
        result = np.tensordot(P, T, axes=[1, 0]).swapaxes(0, 1)
        result = result.reshape(result.shape[0], -1)
        return result

    def test_case_1(self):
        np.random.seed(0)
        P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        T = np.random.rand(3, 4, 4)
        result = task_func(P, T)
        manual_result = self.tensor_product_manual(P, T)
        scaler = StandardScaler().fit(manual_result)
        reversed_result = scaler.inverse_transform(result)
        self.assertEqual(result.shape, (4, 12))
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-05))
        self.assertTrue(np.allclose(manual_result, reversed_result, atol=1e-05))

    def test_case_2(self):
        np.random.seed(0)
        P = np.array([[1, 2], [3, 4], [5, 6]])
        T = np.random.rand(3, 5, 5)
        with self.assertRaises(ValueError):
            task_func(P, T)

    def test_case_3(self):
        np.random.seed(0)
        P = np.eye(4)
        T = np.random.rand(4, 6, 6)
        result = task_func(P, T)
        manual_result = self.tensor_product_manual(P, T)
        scaler = StandardScaler().fit(manual_result)
        reversed_result = scaler.inverse_transform(result)
        self.assertEqual(result.shape, (6, 24))
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-05))
        self.assertTrue(np.allclose(manual_result, reversed_result, atol=1e-05))
