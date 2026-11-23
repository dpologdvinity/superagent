from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result, _ = task_func((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2)
        expected = 2781259372192376861719959017613164544000000000
        self.assertEqual(result, expected)

    def test_case_2(self):
        result, sums = task_func((1, 2, 3), 2)
        expected = 60
        self.assertEqual(result, expected)
        self.assertEqual(list(sums), [5, 4])
        self.assertIsInstance(sums, Series)

    def test_case_3(self):
        result, _ = task_func((1, 2, 3), 5)
        expected = 1
        self.assertEqual(result, expected)
