from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np

class TestCases(unittest.TestCase):

    def test_non_empty_arrays(self):
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])
        result = task_func(array1, array2)
        self.assertAlmostEqual(result, 2.8284271247461903, places=6)

    def test_empty_arrays(self):
        array1 = np.array([])
        array2 = np.array([])
        result = task_func(array1, array2)
        self.assertEqual(result, 0)

    def test_single_element_arrays(self):
        array1 = np.array([1])
        array2 = np.array([2])
        result = task_func(array1, array2)
        self.assertEqual(result, 0)
