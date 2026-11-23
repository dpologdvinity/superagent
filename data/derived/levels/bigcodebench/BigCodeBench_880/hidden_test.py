from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def test_nonnumeric(self):
        data = pd.DataFrame({
            'a': [1, 2, 3],
            'b': ['a', 2, 4]
        })
        self.assertRaises(Exception, task_func, data)
    def test_case_1(self):
        np.random.seed(12)
        data = pd.DataFrame(np.random.randint(0, 20, size=(20, 4)), columns=list('ABCD'))
        labels, kmeans = task_func(data, n_clusters=4, seed=1)
        unique_labels = np.unique(labels)
        assert all(label in range(4) for label in unique_labels)
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
    def test_case_3(self):
        data = pd.DataFrame({'A': range(100), 'B': range(100), 'C': range(100)})
        labels, kmeans = task_func(data, seed=42)
        self.assertIsInstance(kmeans, KMeans)
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        np.testing.assert_equal(labels, expected)
        self.assertTrue(isinstance(labels, np.ndarray))
    def test_case_4(self):
        np.random.seed(5)
        data = pd.DataFrame(np.random.rand(100, 20))
        labels, kmeans = task_func(data, n_clusters=12, seed=12)
        self.assertIsInstance(kmeans, KMeans)
        expected = [ 4,  5,  5,  9, 10,  1,  0,  3,  4,  7,  7,  2, 11, 11,  3,  0,  4,
                    2,  3,  2,  2, 10, 10,  8,  5,  9, 11,  5,  0,  8, 11,  5,  7,  0,
                    8, 11,  7, 11,  6,  1,  1,  7,  0,  9,  3,  7,  8,  0,  4,  1,  7,
                    2, 10,  3, 11,  9,  1,  1,  7,  4,  5,  7,  6,  9,  8,  6,  5,  9,  0,
                    11 , 1 , 1,  4,  2,  1,  0,  7,  5,  1,  9,  6,  7, 10, 10,  4,  4,  9,
                    1,  9,  5,  6,  3, 10,  7, 11,  8,  1,  8,  6, 11]
        np.testing.assert_equal(labels, expected)
        self.assertTrue(isinstance(labels, np.ndarray))
    def test_case_5(self):
        data = pd.DataFrame([])
        self.assertRaises(Exception, task_func, data)
