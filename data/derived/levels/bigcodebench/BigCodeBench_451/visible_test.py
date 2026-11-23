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
        self.n_components = 2
        self.N_SAMPLES = 500
        self.N_FEATURES = 50

    def test_case_1(self):
        transformed_data, _ = task_func()
        self.assertEqual(transformed_data.shape, (self.N_SAMPLES, self.n_components))
        np.random.seed(self.seed)
        X = np.random.rand(self.N_SAMPLES, self.N_FEATURES)
        pca = PCA(n_components=self.n_components, random_state=self.seed)
        pca.fit(X)
        self.assertTrue(np.sum(pca.explained_variance_ratio_) <= 1)

    def test_case_2(self):
        _, heatmap_axes = task_func()
        self.assertIsNotNone(heatmap_axes)
        self.assertIsInstance(heatmap_axes, plt.Axes)
        self.assertEqual(len(heatmap_axes.get_xticklabels()), 2)
        self.assertEqual(len(heatmap_axes.get_yticklabels()), 2)

    def test_case_3(self):
        for n_components in [1, 10, self.N_FEATURES]:
            transformed_data, _ = task_func(n_components=n_components, N_FEATURES=self.N_FEATURES)
            self.assertEqual(transformed_data.shape, (self.N_SAMPLES, n_components))

    def tearDown(self):
        plt.close('all')
