from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data = np.array([[1, 1], [1.1, 1.1], [5, 5], [5.1, 5.1]])
        result = task_func(data, 2)
        self.assertEqual(len(result), 2)
        self.assertTrue(isinstance(result[0], np.ndarray))
        self.assertTrue(isinstance(result[1], np.ndarray))
        result_list = [x.tolist() for x in result.values()]
        self.assertCountEqual(result_list, [[0, 1], [2, 3]])
    def test_case_2(self):
        data = np.array([[1, 2], [1, 3],[1, 4], [1, 5], [200, 1], [200, 2], [200, 3], [3000, 1], [3000, 3]])
        result = task_func(data, 3)
        self.assertEqual(len(result), 3)
        self.assertTrue(isinstance(result[0], np.ndarray))
        self.assertTrue(isinstance(result[1], np.ndarray))
        result_list = [x.tolist() for x in result.values()]
        self.assertCountEqual(result_list, [[0, 1, 2, 3], [4, 5, 6], [7, 8]])
    def test_case_3(self):
        data = np.array([[1, 2]])
        result = task_func(data, 1)
        self.assertEqual(len(result), 1)
        self.assertTrue(isinstance(result[0], np.ndarray))
        self.assertCountEqual(list(result.values()), [0])
    def test_case_4(self):
        '''wrong input'''
        self.assertRaises(Exception, task_func, [])
        self.assertRaises(Exception, task_func, 2)
        self.assertRaises(Exception, task_func, [['asv', 1]])
        self.assertRaises(Exception, task_func, {})
    def test_case_5(self):
        data = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
        result = task_func(data, 5)
        self.assertEqual(len(result), 5)
        for i in range(5):
            self.assertTrue(isinstance(result[i], np.ndarray))
        result_list = [x.tolist() for x in result.values()]
        self.assertCountEqual(result_list, [[0], [1], [2], [3], [4]])
