from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from collections import Counter

class TestCases(unittest.TestCase):

    def test_randomness_with_seed(self):
        result1 = task_func(100, seed=1)
        result2 = task_func(100, seed=1)
        self.assertEqual(result1, result2)

    def test_randomness_without_seed(self):
        result1 = task_func(100)
        result2 = task_func(100)
        self.assertNotEqual(result1, result2)

    def test_validity_of_counts(self):
        num_letters = 200
        result = task_func(num_letters, seed=2)
        self.assertEqual(sum(result.values()), num_letters)
