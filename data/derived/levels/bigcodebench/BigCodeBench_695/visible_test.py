from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        transformed_data = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], 2)
        self.assertEqual(transformed_data.shape, (3, 2))

    def test_case_2(self):
        transformed_data = task_func([(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 2)
        self.assertEqual(transformed_data.shape, (3, 2))
        self.assertTrue(np.all(transformed_data == 0))

    def test_case_3(self):
        transformed_data = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], 3)
        self.assertEqual(transformed_data.shape, (3, 3))
