from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np

class TestCases(unittest.TestCase):

    def test_case_1(self):
        np.random.seed(0)
        array, mean, std, ax = task_func()
        self.assertEqual(array.size, ARRAY_SIZE)
        self.assertEqual(mean, 250.7154)
        self.assertEqual(std, 142.85617453522966)
        self.assertEqual(ax.get_title(), 'Histogram of Random Values')

    def test_case_2(self):
        array, mean, std, ax = task_func()
        self.assertEqual(ax.get_xlabel(), 'Val')
        self.assertEqual(ax.get_ylabel(), 'Freq')

    def test_case_3(self):
        np.random.seed(42)
        array, mean, std, ax = task_func()
        self.assertEqual(array[0], 103)
        self.assertEqual(array[-1], 474)
        self.assertEqual(mean, 250.171)
        self.assertEqual(std, 144.01374920124815)
