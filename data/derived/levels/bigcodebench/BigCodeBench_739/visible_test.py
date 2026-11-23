from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_return_type(self):
        result = task_func()
        self.assertIsInstance(result, float)

    def test_rounded_two_decimal(self):
        result = task_func()
        decimal_part = str(result).split('.')[1]
        self.assertTrue(len(decimal_part) <= 2)

    def test_randomness(self):
        random.seed()
        results = {task_func() for _ in range(100)}
        self.assertTrue(len(results) > 1)
