from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
from itertools import chain

class TestCases(unittest.TestCase):

    def test_1(self):
        L = [[1, 2, 3], [4, 5, 6]]
        result = task_func(L)
        flattened = list(chain.from_iterable(L))
        expected_mean = np.mean(flattened)
        expected_variance = np.var(flattened)
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['variance'], expected_variance)

    def test_2(self):
        L = [[10, 20], [30, 40], [50, 60]]
        result = task_func(L)
        flattened = list(chain.from_iterable(L))
        expected_mean = np.mean(flattened)
        expected_variance = np.var(flattened)
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['variance'], expected_variance)

    def test_3(self):
        L = [[5]]
        result = task_func(L)
        flattened = list(chain.from_iterable(L))
        expected_mean = np.mean(flattened)
        expected_variance = np.var(flattened)
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['variance'], expected_variance)
