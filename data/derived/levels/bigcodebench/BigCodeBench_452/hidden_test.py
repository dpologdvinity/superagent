from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import datasets
from numpy.testing import assert_array_equal
import numpy as np
class TestCases(unittest.TestCase):
    def generate_data(self, n_samples, n_features, random_seed=None):
        # Generate data for testing
        X, y = datasets.make_regression(
            n_samples=n_samples,
            n_features=n_features,
            noise=0.1,
            random_state=random_seed,
        )
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=random_seed
        )
        return X_train, X_test, y_train, y_test
    def test_case_1(self):
        # Basic test for different inputs
        random_seed = 1
        for n_samples, n_features in [
            [100, 5],
            [500, 8],
            [1000, 10],
            [5000, 15],
            [10000, 20],
        ]:
            predictions, _, _, mse = task_func(n_samples, n_features, random_seed=random_seed)
            _, _, _, y = self.generate_data(
                n_samples, n_features, random_seed=random_seed
            )
            self.assertEqual(mse, mean_squared_error(y, predictions))
    def test_case_2(self):
        # Test default parameters
        predictions, coefficients, intercept, mse = task_func(random_seed=42)
        self.assertEqual(
            predictions.shape[0], 20
        )  # Default split leaves 20% of 100 samples for testing
        self.assertEqual(coefficients.shape[0], 10)  # Default number of features
        self.assertIsInstance(intercept, float)
        _, _, _, y = self.generate_data(
                100, 10, 42
            )
        self.assertEqual(mse, mean_squared_error(y, predictions))
    def test_case_3(self):
        # Test different random seeds for reproducibility
        _, coefficients_1, intercept_1, mse_1 = task_func(random_seed=1)
        _, coefficients_2, intercept_2, mse_2 = task_func(random_seed=2)
        with self.assertRaises(AssertionError):
            assert_array_equal(coefficients_1, coefficients_2)
            self.assertEqual(intercept_1, intercept_2)
            
    def test_case_4(self):
        # Test zero and negative samples and features
        with self.assertRaises(ValueError):
            task_func(n_samples=0, n_features=10)
        with self.assertRaises(ValueError):
            task_func(n_samples=100, n_features=0)
        with self.assertRaises(ValueError):
            task_func(n_samples=-100, n_features=10)
        with self.assertRaises(ValueError):
            task_func(n_samples=100, n_features=-10)
    def test_case_5(self):
        # Test extreme values for parameters
        predictions, _, _, mse = task_func(n_samples=100000, n_features=100, random_seed=42)
        self.assertEqual(
            predictions.shape[0], 20000
        )  # 20% of 100000 samples for testing
        self.assertAlmostEqual(mse, 0.010142327812255192, places=4)
        
    def test_case_6(self):
        # Test output shapes
        predictions, coefficients, _, mse = task_func(
            n_samples=100, n_features=5, random_seed=42
        )
        self.assertEqual(predictions.shape[0], 20)
        self.assertEqual(coefficients.shape[0], 5)
    def test_case_7(self):
        # Test output types
        predictions, coefficients, intercept, mse = task_func()
        self.assertIsInstance(predictions, np.ndarray)
        self.assertIsInstance(coefficients, np.ndarray)
        self.assertIsInstance(intercept, float)
        self.assertIsInstance(mse, float)
        
    def test_case_8(self):
        # Test determinism with the same random seed
        predictions_1, _, _, mse_1 = task_func(random_seed=42)
        predictions_2, _, _, mse_2 = task_func(random_seed=42)
        assert_array_equal(predictions_1, predictions_2)
        self.assertEqual(mse_1, mse_2)
        
    def test_case_9(self):
        # Test without random seed (non-deterministic outcomes)
        predictions_1, _, _, _ = task_func()
        predictions_2, _, _, _ = task_func()
        with self.assertRaises(AssertionError):
            assert_array_equal(predictions_1, predictions_2)
