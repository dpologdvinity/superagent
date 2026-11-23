from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_1(self):
        result = task_func([1, 2, 3], [3, 2, 1], 1000)
        self.assertTrue(set(result.keys()) == {1, 2, 3})

    def test_2(self):
        result = task_func([1, 2], [1, 1], 500)
        self.assertTrue(set(result.keys()) == {1, 2})

    def test_3(self):
        result = task_func([1], [1], 300)
        self.assertTrue(result == {1: 300})
