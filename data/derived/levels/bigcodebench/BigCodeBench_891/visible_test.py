from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import pandas as pd
import tempfile
import os
from sklearn.linear_model import LinearRegression

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv')
        self.csv_file_path = self.temp_file.name
        self.temp_file.close()

    def tearDown(self):
        os.unlink(self.csv_file_path)

    def create_csv(self, data, header=True):
        df = pd.DataFrame(data)
        df.to_csv(self.csv_file_path, index=False, header=header)

    def test_valid_data(self):
        data = {'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [7, 8, 9]}
        self.create_csv(data)
        model, predictions = task_func(self.csv_file_path, 'target')
        self.assertIsInstance(model, LinearRegression)
        self.assertIsInstance(predictions, np.ndarray)
        self.assertEqual(len(predictions), 1)

    def test_different_test_size(self):
        data = {'feature1': range(10), 'feature2': range(10, 20), 'target': range(20, 30)}
        self.create_csv(data)
        model, predictions = task_func(self.csv_file_path, 'target', test_size=0.3)
        self.assertEqual(len(predictions), 3)

    def test_invalid_attribute(self):
        data = {'feature1': [1, 2], 'feature2': [3, 4]}
        self.create_csv(data)
        with self.assertRaises(KeyError):
            task_func(self.csv_file_path, 'nonexistent_target')
