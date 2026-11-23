from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def _calculate_sum_of_product_pairs(self, matrix):
        values = matrix.flatten()
        all_pairs = list(combinations(values, 2))
        sum_of_products = reduce(lambda a, b: a + b, [np.prod(pair) for pair in all_pairs])
        return sum_of_products

    def test_case_1(self):
        result, matrix = task_func(seed=1)
        self.assertAlmostEqual(result, self._calculate_sum_of_product_pairs(matrix))

    def test_case_2(self):
        seed = 42
        result1, matrix1 = task_func(seed=seed)
        result2, matrix2 = task_func(seed=seed)
        self.assertEqual(result1, result2)
        self.assertEqual(list(matrix1.flatten()), list(matrix2.flatten()))

    def test_case_3(self):
        shape = (4, 4)
        result, matrix = task_func(shape=shape, seed=1)
        self.assertAlmostEqual(result, self._calculate_sum_of_product_pairs(matrix))
