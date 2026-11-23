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
        
    def test_case_4(self):
        np.random.seed(142)
        array, mean, std, ax = task_func()
        self.assertEqual(array[0], 278)
        self.assertEqual(array[-1], 113)
        self.assertEqual(mean, 251.1245)
        self.assertEqual(std, 144.49066405740547)
    def test_case_5(self):
        np.random.seed(250)
        array, mean, std, ax = task_func()
        self.assertEqual(array[0], 367)
        self.assertEqual(array[-1], 190)
        self.assertEqual(mean, 249.037)
        self.assertEqual(std, 144.32681882103546)
