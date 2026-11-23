from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
class TestCases(unittest.TestCase):
    def setUp(self):
        self.seed = 42
        # default parameters
        self.n_components = 2
        self.N_SAMPLES = 500
        self.N_FEATURES = 50
    def test_case_1(self):
        # Test basic functionality - results
        transformed_data, _ = task_func()
        self.assertEqual(transformed_data.shape, (self.N_SAMPLES, self.n_components))
        np.random.seed(self.seed)
        X = np.random.rand(self.N_SAMPLES, self.N_FEATURES)
        pca = PCA(n_components=self.n_components, random_state=self.seed)
        pca.fit(X)
        self.assertTrue(np.sum(pca.explained_variance_ratio_) <= 1)
    def test_case_2(self):
        # Test basic functionality - visualization
        _, heatmap_axes = task_func()
        self.assertIsNotNone(heatmap_axes)
        self.assertIsInstance(heatmap_axes, plt.Axes)
        self.assertEqual(len(heatmap_axes.get_xticklabels()), 2)
        self.assertEqual(len(heatmap_axes.get_yticklabels()), 2)
    def test_case_3(self):
        # Test n_components
        for n_components in [1, 10, self.N_FEATURES]:
            transformed_data, _ = task_func(
                n_components=n_components, N_FEATURES=self.N_FEATURES
            )
            self.assertEqual(transformed_data.shape, (self.N_SAMPLES, n_components))
    def test_case_4(self):
        # Test N_SAMPLES
        for n_samples in [self.n_components, 10, 50, 100]:
            transformed_data, _ = task_func(N_SAMPLES=n_samples)
            self.assertEqual(transformed_data.shape, (n_samples, self.n_components))
    def test_case_5(self):
        # Test N_FEATURES
        for n_features in [self.n_components, 10, 50, 100]:
            transformed_data, _ = task_func(N_FEATURES=n_features)
            self.assertEqual(
                transformed_data.shape, (self.N_SAMPLES, self.n_components)
            )
    def test_case_6(self):
        # Test random_seed
        transformed_data1, _ = task_func(random_seed=self.seed)
        transformed_data2, _ = task_func(random_seed=self.seed)
        np.testing.assert_array_equal(transformed_data1, transformed_data2)
        transformed_data2, _ = task_func(random_seed=0)
        with self.assertRaises(AssertionError):
            np.testing.assert_array_equal(transformed_data1, transformed_data2)
    def test_case_7(self):
        # Function should fail at invalid values
        with self.assertRaises(ValueError):
            # negative n_components
            task_func(n_components=-1)
        with self.assertRaises(ValueError):
            # more components than features
            task_func(n_components=self.N_FEATURES + 10, N_FEATURES=self.N_FEATURES)
    def tearDown(self):
        plt.close("all")
