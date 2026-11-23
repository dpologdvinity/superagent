from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Default values
        result, _ = task_func((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2)
        expected = 2781259372192376861719959017613164544000000000
        self.assertEqual(result, expected)
    def test_case_2(self):
        # Custom tuple and subset size
        result, sums = task_func((1, 2, 3), 2)
        expected = 60
        self.assertEqual(result, expected)
        # Test the top sums
        self.assertEqual(list(sums), [5, 4])
        # Test the type of the top sums
        self.assertIsInstance(sums, Series)
    def test_case_3(self):
        # Larger subset size than tuple length
        result, _ = task_func((1, 2, 3), 5)
        expected = 1  # No subset of size 5 can be formed, so the product will be 1
        self.assertEqual(result, expected)
    def test_case_4(self):
        # Subset size of 0
        result, sums = task_func((1, 2, 3), 0)
        expected = 1  # No subset of size 0 can be formed, so the product will be 1
        self.assertEqual(result, expected)
        self.assertEqual(list(sums), [])
    def test_case_5(self):
        # Larger tuple
        result, _ = task_func((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), 4)
        self.assertIsInstance(result, int)  # Ensure the result is an integer
