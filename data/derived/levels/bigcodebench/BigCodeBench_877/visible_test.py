from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np

class TestCases(unittest.TestCase):

    def setUp(self):
        np.random.seed(42)
        self.data_small = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20]})
        self.data_large = pd.DataFrame(np.random.randint(0, 100, size=(1000, 50)))

    def test_basic_functionality(self):
        result = task_func(self.data_small)
        self.assertEqual(result.shape, (5, 2))

    def test_varying_components(self):
        for components in [1, 3, 4]:
            result = task_func(self.data_small, n_components=components)
            self.assertEqual(result.shape, (5, components))

    def test_large_dataset(self):
        result = task_func(self.data_large, n_components=10)
        self.assertEqual(result.shape, (1000, 10))
