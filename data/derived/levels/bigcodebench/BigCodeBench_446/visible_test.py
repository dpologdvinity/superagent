from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        n_samples, n_features, centers = (100, 2, 3)
        X, y, ax = task_func()
        self.assertEqual(X.shape, (n_samples, n_features))
        self.assertEqual(y.shape, (n_samples,))
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(set(y)), centers)

    def test_case_2(self):
        for n_samples in [1, 50, 100]:
            X, y, _ = task_func(n_samples=n_samples)
            self.assertEqual(X.shape[0], n_samples)
            self.assertEqual(y.shape[0], n_samples)

    def test_case_3(self):
        for centers in [1, 50, 100]:
            _, y, _ = task_func(centers=centers)
        self.assertEqual(len(set(y)), centers)

    def tearDown(self):
        plt.close('all')
