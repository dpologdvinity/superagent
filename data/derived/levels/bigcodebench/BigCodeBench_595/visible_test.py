from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from array import array

class TestCases(unittest.TestCase):

    def test_return_type(self):
        nums, pos = task_func(5, 50)
        self.assertIsInstance(nums, array)
        self.assertIsInstance(pos, int)

    def test_correct_length(self):
        nums, _ = task_func(5, 50)
        self.assertEqual(len(nums), 5)

    def test_sum_of_numbers(self):
        nums, _ = task_func(5, 50)
        self.assertEqual(sum(nums), 50)
