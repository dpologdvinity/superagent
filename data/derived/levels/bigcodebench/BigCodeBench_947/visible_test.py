from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy.testing as npt

class TestCases(unittest.TestCase):

    def test_case_1(self):
        matrix = task_func(seed=0)
        self.assertEqual(matrix.shape, (3, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) > 0))

    def test_case_2(self):
        matrix = task_func(2, 2, datetime(2021, 1, 1), datetime(2021, 1, 10), seed=42)
        self.assertEqual(matrix.shape, (2, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))

    def test_case_3(self):
        matrix = task_func(4, 4, datetime(2000, 1, 1), datetime(2021, 12, 31), seed=55)
        self.assertEqual(matrix.shape, (4, 4))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))
