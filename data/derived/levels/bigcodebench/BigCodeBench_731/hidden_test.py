from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
from sklearn.datasets import make_classification
import numpy as np
import unittest
import sys
sys.path.append("/mnt/data")
# Defining the test function
class TestCases(unittest.TestCase):
    def test_save_and_load_data(self):
        data, target = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data))
        self.assertTrue(np.array_equal(target, loaded_target))
    
    def test_save_and_load_empty_data(self):
        data, target = np.array([]), np.array([])
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data))
        self.assertTrue(np.array_equal(target, loaded_target))
    
    def test_save_and_load_single_element_data(self):
        data, target = np.array([5]), np.array([1])
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data))
        self.assertTrue(np.array_equal(target, loaded_target))
    
    def test_save_and_load_large_data(self):
        data, target = make_classification(n_samples=1000, n_features=50, n_informative=5, n_redundant=25, n_classes=3, random_state=2)
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data))
        self.assertTrue(np.array_equal(target, loaded_target))
    
    def test_save_and_load_random_data(self):
        data, target = np.random.rand(50, 5), np.random.randint(0, 2, 50)
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data))
        self.assertTrue(np.array_equal(target, loaded_target))
