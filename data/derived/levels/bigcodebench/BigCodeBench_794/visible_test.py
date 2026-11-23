from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import string

class TestCases(unittest.TestCase):

    def setUp(self):
        self.BRACKETS = '(){}[]'
        return

    def test_rng(self):
        res1 = task_func(100, random_seed=42)
        res2 = task_func(100, random_seed=42)
        self.assertEqual(res1, res2)

    def test_case_1(self):
        result = task_func(5, random_seed=1)
        self.assertEqual(len(result), 5)
        for char in result:
            self.assertIn(char, string.ascii_lowercase + self.BRACKETS)

    def test_case_2(self):
        result = task_func(0, random_seed=2)
        self.assertEqual(len(result), 0)
