from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from collections import Counter

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        result = task_func(input_data)
        self.assertIsInstance(result, Counter, 'The result should be a Counter object')
        self.assertEqual(sum(result.values()), 30, 'The total count should be 30')
        self.assertEqual(len(result), len(set(input_data)), 'All unique elements should be present in the result')

    def test_case_2(self):
        input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = task_func(input_data)
        self.assertIsInstance(result, Counter, 'The result should be a Counter object')
        self.assertEqual(sum(result.values()), 30, 'The total count should be 30')
        self.assertEqual(len(result), len(set(input_data)), 'All unique elements should be present in the result')

    def test_case_3(self):
        input_data = ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
        result = task_func(input_data)
        self.assertIsInstance(result, Counter, 'The result should be a Counter object')
        self.assertEqual(sum(result.values()), 30, 'The total count should be 30')
        self.assertEqual(len(result), 2, 'The result should contain two unique elements for repeated input')
