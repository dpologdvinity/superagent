from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

class TestCases(unittest.TestCase):

    def test_basic_functionality(self):
        random.seed(0)
        result = task_func(3, 5)
        self.assertLessEqual(len(result), 3)
        for key in result:
            self.assertIn(key, LETTERS)
            self.assertEqual(result[key], [1, 2, 3, 4, 5])

    def test_no_keys(self):
        random.seed(0)
        result = task_func(0, 5)
        self.assertEqual(result, {})

    def test_no_values(self):
        random.seed(0)
        result = task_func(3, 0)
        for key in result:
            self.assertEqual(result[key], [])
