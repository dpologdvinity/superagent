from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random

class TestCases(unittest.TestCase):

    def test_default_parameters(self):
        random.seed(0)
        train_data, test_data = task_func()
        self.assertEqual(len(train_data), 8000)
        self.assertEqual(len(test_data), 2000)

    def test_custom_parameters(self):
        random.seed(0)
        train_data, test_data = task_func(n_data_points=500, min_value=1.0, max_value=5.0, test_size=0.3)
        self.assertEqual(len(train_data), 350)
        self.assertEqual(len(test_data), 150)
        self.assertTrue(train_data['Value'].between(1.0, 5.0).all())
        self.assertTrue(test_data['Value'].between(1.0, 5.0).all())

    def test_train_test_size_ratio(self):
        random.seed(0)
        n_data_points = 1000
        test_size = 0.25
        train_data, test_data = task_func(n_data_points=n_data_points, test_size=test_size)
        expected_train_size = int(n_data_points * (1 - test_size))
        expected_test_size = n_data_points - expected_train_size
        self.assertEqual(len(train_data), expected_train_size)
        self.assertEqual(len(test_data), expected_test_size)
