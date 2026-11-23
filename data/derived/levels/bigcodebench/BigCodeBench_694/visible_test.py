from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        combination = task_func((1, 2, 3, 4), 2)
        self.assertTrue(tuple(sorted(combination)) in [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])

    def test_case_2(self):
        combination = task_func((1, 2, 3, 4), 3)
        self.assertTrue(tuple(sorted(combination)) in [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)])

    def test_case_3(self):
        combination = task_func((1, 2, 3, 4), 4)
        self.assertTrue(tuple(sorted(combination)) in [(1, 2, 3, 4)])
