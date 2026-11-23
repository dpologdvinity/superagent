from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from collections import Counter

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = task_func([])
        self.assertEqual(result, [])

    def test_case_2(self):
        result = task_func([[], [], []])
        for basket in result:
            self.assertEqual(basket, Counter())

    def test_case_3(self):
        result = task_func([[1], [1, 2], [1, 2, 3]])
        self.assertEqual(len(result), 3)
        self.assertEqual(sum(result[0].values()), 1)
        self.assertEqual(sum(result[1].values()), 2)
        self.assertEqual(sum(result[2].values()), 3)
