from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
from random import seed, shuffle
import itertools

class TestCases(unittest.TestCase):

    def test_default_numbers(self):
        result = task_func()
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)

    def test_custom_list(self):
        result = task_func([1, 2, 3])
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)

    def test_negative_numbers(self):
        result = task_func([-3, -2, -1])
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)
