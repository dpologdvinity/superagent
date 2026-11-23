from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from collections import Counter

class TestCases(unittest.TestCase):

    def test_case_1(self):
        """Single tuple with small integers as strings"""
        T1 = (('1', '2', '3'),)
        result = task_func(T1)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 6)

    def test_case_2(self):
        """Multiple tuples with small integers as strings"""
        T1 = (('1', '2'), ('3', '4'))
        result = task_func(T1)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 10)

    def test_case_3(self):
        """Single tuple with larger integers as strings"""
        T1 = (('10', '20', '30'),)
        result = task_func(T1)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 60)
