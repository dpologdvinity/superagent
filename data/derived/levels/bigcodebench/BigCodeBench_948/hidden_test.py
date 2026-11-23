from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        result = task_func()
        self.assertEqual(result.shape, (3, 2))
        self.assertTrue(np.all(result >= 0))
    
    def test_case_2(self):
        result = task_func(2, 2)
        self.assertEqual(result.shape, (2, 2))
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))
        
    def test_case_3(self):
        result = task_func(4, 3)
        self.assertEqual(result.shape, (4, 3))
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))
    
    def test_case_4(self):
        result = task_func(5, 1)
        self.assertEqual(result.shape, (5, 1))
        self.assertTrue(np.all(result >= 0))
        
    def test_case_5(self):
        result = task_func(1, 5)
        self.assertEqual(result.shape, (1, 5))
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))
