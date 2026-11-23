from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import numpy as np
import unittest
import re

class TestCases(unittest.TestCase):
    """
    Define test cases for the task_func function.
    """

    def test_case_1(self):
        arr = np.array(['apple.orange', 'red.green.yellow'])
        result = task_func(arr)
        expected = np.array(['orange.apple', 'yellow.green.red'])
        np.testing.assert_array_equal(result, expected)

    def test_case_2(self):
        arr = np.array(['hello.world', 'this.is.a.test'])
        result = task_func(arr)
        expected = np.array(['world.hello', 'test.a.is.this'])
        np.testing.assert_array_equal(result, expected)

    def test_case_3(self):
        arr = np.array(['hello', 'world'])
        result = task_func(arr)
        expected = np.array(['hello', 'world'])
        np.testing.assert_array_equal(result, expected)
