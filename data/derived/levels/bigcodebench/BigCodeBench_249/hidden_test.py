from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        random.seed(0)
        train_data, test_data = task_func()
        self.assertEqual(len(train_data), 8000)  # 80% of 10000
        self.assertEqual(len(test_data), 2000)  # 20% of 10000
    def test_custom_parameters(self):
        random.seed(0)
        train_data, test_data = task_func(n_data_points=500, min_value=1.0, max_value=5.0, test_size=0.3)
        self.assertEqual(len(train_data), 350)  # 70% of 500
        self.assertEqual(len(test_data), 150)  # 30% of 500
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
    def test_value_range(self):
        random.seed(0)
        min_value = 2.0
        max_value = 3.0
        train_data, _ = task_func(min_value=min_value, max_value=max_value)
        self.assertTrue(train_data['Value'].between(min_value, max_value).all())
    def test_value_precision(self):
        random.seed(0)
        train_data, _ = task_func()
        all_three_decimal = all(train_data['Value'].apply(lambda x: len(str(x).split('.')[1]) == 3))
        self.assertFalse(all_three_decimal)
