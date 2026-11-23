from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np

class TestCases(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({'Column1': np.random.rand(10), 'Column2': np.random.rand(10)})

    def test_transformed_data_shape(self):
        transformed_data, _ = task_func(self.data, 2)
        self.assertEqual(transformed_data.shape, (10, 2))

    def test_invalid_n_components(self):
        with self.assertRaises(ValueError):
            task_func(self.data, 0)

    def test_invalid_n_components_type(self):
        with self.assertRaises(ValueError):
            task_func(self.data, 'two')
