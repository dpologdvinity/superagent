from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with empty list
        result = task_func([])
        self.assertEqual(result, [])
    def test_case_2(self):
        # Testing with empty sublists
        result = task_func([[], [], []])
        for basket in result:
            self.assertEqual(basket, Counter())
        
    def test_case_3(self):
        # Testing with sublists of different lengths
        result = task_func([[1], [1, 2], [1, 2, 3]])
        self.assertEqual(len(result), 3)
        self.assertEqual(sum(result[0].values()), 1)
        self.assertEqual(sum(result[1].values()), 2)
        self.assertEqual(sum(result[2].values()), 3)
    def test_case_4(self):
        # Testing with sublists containing the same element
        result = task_func([[1, 1, 1], [2, 2, 2, 2]])
        self.assertEqual(len(result), 2)
        self.assertEqual(sum(result[0].values()), 3)
        self.assertEqual(sum(result[1].values()), 4)
        
    def test_case_5(self):
        # Testing with large sublists
        result = task_func([[1]*100, [2]*200])
        self.assertEqual(len(result), 2)
        self.assertEqual(sum(result[0].values()), 100)
        self.assertEqual(sum(result[1].values()), 200)
