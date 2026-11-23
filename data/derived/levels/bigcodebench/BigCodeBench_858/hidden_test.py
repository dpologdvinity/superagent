from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_randomness_with_seed(self):
        # Using a seed should give consistent results
        result1 = task_func(100, seed=1)
        result2 = task_func(100, seed=1)
        self.assertEqual(result1, result2)
    def test_randomness_without_seed(self):
        # Without a seed, the results should be potentially different
        result1 = task_func(100)
        result2 = task_func(100)
        self.assertNotEqual(result1, result2)
    def test_validity_of_counts(self):
        # The total counts should equal the number of letters generated
        num_letters = 200
        result = task_func(num_letters, seed=2)
        self.assertEqual(sum(result.values()), num_letters)
    def test_non_negative_counts(self):
        # All counts should be non-negative
        result = task_func(100, seed=3)
        self.assertTrue(all(count >= 0 for count in result.values()))
    def test_type_of_return_value(self):
        # The return type should be a Counter object
        result = task_func(100, seed=4)
        self.assertIsInstance(result, Counter)
    def test_return_value(self):
        # test specific values
        result = task_func(10, seed=42)
        exp = Counter({'d': 2, 'x': 2, 'h': 2, 'u': 1, 'a': 1, 'i': 1, 'e': 1})
        self.assertEqual(result, exp)
