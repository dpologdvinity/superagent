from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame([[14, 25], [1, 22], [7, 8], [10, 15]], columns=['Latitude', 'Longitude'])
        self.target = [10, 15]

    def test_correct_number_of_neighbors(self):
        k = 2
        result = task_func(self.data, self.target, k)
        self.assertEqual(len(result), k)

    def test_correct_neighbors(self):
        result = task_func(self.data, self.target, 1)
        self.assertEqual(result, [[10, 15]])

    def test_invalid_k_value_negative(self):
        with self.assertRaises(ValueError):
            task_func(self.data, self.target, -1)
