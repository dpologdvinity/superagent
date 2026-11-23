from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
import numpy as np

class TestCases(unittest.TestCase):

    def setUp(self):
        self.default_seed = 42
        self.large_n_samples = 100000
        self.small_n_samples = 100
        self.zero_n_samples = 0
        self.negative_n_samples = -100
        self.default_mu = 0
        self.default_sigma = 1
        self.large_sigma = 5
        self.small_sigma = 0.2
        self.zero_sigma = 0
        self.negative_sigma = -1
        self.custom_mu = 5
        self.custom_sigma = 2

    def test_case_1(self):
        mu_test = 3
        sigma_test = 2
        n_samples_test = 10000
        random_seed_test = 42
        _, samples = task_func(n_samples=n_samples_test, mu=mu_test, sigma=sigma_test, random_seed=random_seed_test)
        sample_mean = np.mean(samples)
        sample_std = np.std(samples)
        self.assertAlmostEqual(sample_mean, mu_test, places=1, msg='Sample mean does not match expected mean.')
        self.assertAlmostEqual(sample_std, sigma_test, places=1, msg='Sample standard deviation does not match expected sigma.')

    def test_case_2(self):
        ax, _ = task_func(random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 30)

    def test_case_3(self):
        ax, _ = task_func(n_samples=self.small_n_samples, mu=self.custom_mu, sigma=self.custom_sigma, random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 30)

    def tearDown(self):
        plt.close('all')
