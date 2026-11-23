from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from collections import deque

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_list = ['A', 'B', 'C', 'D', 'E']
        expected_output = deque(['C', 'D', 'E', 'A', 'B'])
        result = task_func(input_list)
        self.assertEqual(result, expected_output, 'Test Case 1 Failed')

    def test_case_2(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = deque([3, 4, 5, 1, 2])
        result = task_func(input_list)
        self.assertEqual(result, expected_output, 'Test Case 2 Failed')

    def test_case_3(self):
        input_list = []
        expected_output = deque([])
        result = task_func(input_list)
        self.assertEqual(result, expected_output, 'Test Case 3 Failed')
