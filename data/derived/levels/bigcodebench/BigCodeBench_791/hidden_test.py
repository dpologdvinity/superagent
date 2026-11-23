from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test Description: Testing with a list of unique string elements
        # Input: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        # Expected Output: A Counter object with 30 elements, all unique elements of the input should be present
        input_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        result = task_func(input_data)
        self.assertIsInstance(result, Counter, "The result should be a Counter object")
        self.assertEqual(sum(result.values()), 30, "The total count should be 30")
        self.assertEqual(len(result), len(set(input_data)), "All unique elements should be present in the result")
    def test_case_2(self):
        # Test Description: Testing with a list of unique integer elements
        # Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Expected Output: A Counter object with 30 elements, all unique elements of the input should be present
        input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = task_func(input_data)
        self.assertIsInstance(result, Counter, "The result should be a Counter object")
        self.assertEqual(sum(result.values()), 30, "The total count should be 30")
        self.assertEqual(len(result), len(set(input_data)), "All unique elements should be present in the result")
    def test_case_3(self):
        # Test Description: Testing with a list with repeated elements
        # Input: ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
        # Expected Output: A Counter object with 30 elements, two unique elements should be present ('A' and 'B')
        input_data = ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
        result = task_func(input_data)
        self.assertIsInstance(result, Counter, "The result should be a Counter object")
        self.assertEqual(sum(result.values()), 30, "The total count should be 30")
        self.assertEqual(len(result), 2, "The result should contain two unique elements for repeated input")
    def test_empty_list(self):
        input_data = []
        result = task_func(input_data)
        self.assertIsInstance(result, Counter, "The result should be a Counter object even for an empty list")
        self.assertEqual(len(result), 0, "The result should be an empty Counter for an empty input list")
    def test_case_5(self):
        # Test Description: Testing with a list of mixed data types
        # Input: ['A', 2, 'C', 4, 'E', 6, 'G', 8, 'I', 10]
        # Expected Output: A Counter object with 30 elements
        input_data = ['A', 2, 'C', 4, 'E', 6, 'G', 8, 'I', 10]
        result = task_func(input_data)
        self.assertIsInstance(result, Counter, "The result should be a Counter object when input has mixed types")
