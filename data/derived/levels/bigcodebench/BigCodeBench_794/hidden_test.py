from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import string
class TestCases(unittest.TestCase):
    def setUp(self):
        self.BRACKETS = "(){}[]"
        return 
    def test_rng(self):
        # rng reproducability
        res1 = task_func(100, random_seed=42)
        res2 = task_func(100, random_seed=42)
        self.assertEqual(res1, res2)
    def test_case_1(self):
        # Testing with length = 5
        result = task_func(5, random_seed=1)
        self.assertEqual(len(result), 5)
        for char in result:
            self.assertIn(char, string.ascii_lowercase + self.BRACKETS)
    def test_case_2(self):
        # Testing with length = 0 (edge case)
        result = task_func(0, random_seed=2)
        self.assertEqual(len(result), 0)
    def test_case_3(self):
        # Testing with length = 10
        result = task_func(10, random_seed=3)
        self.assertEqual(len(result), 10)
        for char in result:
            self.assertIn(char, string.ascii_lowercase + self.BRACKETS)
    def test_case_4(self):
        # Testing with length = 1 (edge case)
        result = task_func(1, random_seed=34)
        self.assertEqual(len(result), 1)
        self.assertIn(result, string.ascii_lowercase + self.BRACKETS)
    def test_case_5(self):
        # Testing with length = 50
        result = task_func(50, random_seed=777)
        self.assertEqual(len(result), 50)
        for char in result:
            self.assertIn(char, string.ascii_lowercase + self.BRACKETS)
