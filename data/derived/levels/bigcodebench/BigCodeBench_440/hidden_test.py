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
        # Reverse normalization for comparison
        scaler = StandardScaler().fit(manual_result)
        reversed_result = scaler.inverse_transform(result)
        self.assertEqual(result.shape, (4, 12))
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-5))
        self.assertTrue(np.allclose(manual_result, reversed_result, atol=1e-5))
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
        # Reverse normalization for comparison
        scaler = StandardScaler().fit(manual_result)
        reversed_result = scaler.inverse_transform(result)
        self.assertEqual(result.shape, (6, 24))
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-5))
        self.assertTrue(np.allclose(manual_result, reversed_result, atol=1e-5))
    def test_case_4(self):
        np.random.seed(0)
        P = np.ones((5, 5))
        T = np.random.rand(5, 7, 7)
        result = task_func(P, T)
        manual_result = self.tensor_product_manual(P, T)
        # Reverse normalization for comparison
        scaler = StandardScaler().fit(manual_result)
        reversed_result = scaler.inverse_transform(result)
        self.assertEqual(result.shape, (7, 35))
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-5))
        self.assertTrue(np.allclose(manual_result, reversed_result, atol=1e-5))
    def test_case_5(self):
        np.random.seed(0)
        P = np.diag(np.arange(1, 7))
        T = np.random.rand(6, 8, 8)
        result = task_func(P, T)
        manual_result = self.tensor_product_manual(P, T)
        # Reverse normalization for comparison
        scaler = StandardScaler().fit(manual_result)
        reversed_result = scaler.inverse_transform(result)
        self.assertEqual(result.shape, (8, 48))
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-5))
        self.assertTrue(np.allclose(manual_result, reversed_result, atol=1e-5))
    def test_case_6(self):
        # Test with an empty matrix and tensor, expecting a ValueError due to incompatible shapes
        P = np.array([])
        T = np.array([])
        with self.assertRaises(ValueError):
            task_func(P, T)
    def test_case_7(self):
        # Test with non-numeric inputs in matrices/tensors to verify type handling
        P = np.array([["a", "b"], ["c", "d"]])
        T = np.random.rand(2, 2, 2)
        with self.assertRaises(Exception):
            task_func(P, T)
    def test_case_8(self):
        # Test with zero matrix and tensor to verify handling of all-zero inputs
        P = np.zeros((5, 5))
        T = np.zeros((5, 3, 3))
        result = task_func(P, T)
        self.assertTrue(np.allclose(result, np.zeros((3, 15))))
    def test_case_9(self):
        # Test DataFrame output for correct column names, ensuring they match expected feature naming convention
        P = np.random.rand(3, 3)
        T = np.random.rand(3, 4, 4)
        result = task_func(P, T)
        expected_columns = [
            "feature_0",
            "feature_1",
            "feature_2",
            "feature_3",
            "feature_4",
            "feature_5",
            "feature_6",
            "feature_7",
            "feature_8",
            "feature_9",
            "feature_10",
            "feature_11",
        ]
        self.assertListEqual(list(result.columns), expected_columns)
    def test_case_10(self):
        # Test to ensure DataFrame indices start from 0 and are sequential integers
        P = np.random.rand(2, 3)
        T = np.random.rand(3, 5, 5)
        result = task_func(P, T)
        expected_indices = list(range(5))  # Expected indices for 5 rows
        self.assertListEqual(list(result.index), expected_indices)
