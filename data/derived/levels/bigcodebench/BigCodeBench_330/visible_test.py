from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_empty_list(self):
        random.seed(0)
        rand_list, top_k = task_func(0, 3)
        self.assertEqual(rand_list, [])
        self.assertEqual(top_k, [])

    def test_k_larger_than_list_length(self):
        random.seed(0)
        rand_list, top_k = task_func(5, 10)
        self.assertEqual(len(rand_list), 5)
        self.assertEqual(len(top_k), 5)

    def test_sorted_list(self):
        random.seed(0)
        rand_list, top_k = task_func(100, 3)
        self.assertEqual(top_k, sorted(rand_list, reverse=True)[:3])
