from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np

class TestCases(unittest.TestCase):

    def test_nonnumeric(self):
        data = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 2, 4]})
        self.assertRaises(Exception, task_func, data)

    def test_case_1(self):
        np.random.seed(12)
        data = pd.DataFrame(np.random.randint(0, 20, size=(20, 4)), columns=list('ABCD'))
        labels, kmeans = task_func(data, n_clusters=4, seed=1)
        unique_labels = np.unique(labels)
        assert all((label in range(4) for label in unique_labels))
        self.assertTrue(isinstance(labels, np.ndarray))
        self.assertIsInstance(kmeans, KMeans)
        np.testing.assert_equal(labels, [3, 0, 3, 1, 2, 1, 2, 0, 2, 1, 1, 3, 3, 1, 0, 0, 0, 0, 1, 3])

    def test_case_2(self):
        data = pd.DataFrame(np.zeros((100, 4)), columns=list('ABCD'))
        labels, kmeans = task_func(data, n_clusters=3, seed=12)
        self.assertIsInstance(kmeans, KMeans)
        assert len(np.unique(labels)) == 1
        self.assertTrue(isinstance(labels, np.ndarray))
        self.assertCountEqual(labels, np.zeros(100))
