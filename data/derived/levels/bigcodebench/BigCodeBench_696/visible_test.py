from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        points = task_func(1, 3)
        for x, y in points:
            self.assertTrue(x ** 2 + y ** 2 <= 1)

    def test_case_2(self):
        points = task_func(2, 3)
        for x, y in points:
            self.assertTrue(x ** 2 + y ** 2 <= 4)

    def test_case_3(self):
        points = task_func(3, 3)
        for x, y in points:
            self.assertTrue(x ** 2 + y ** 2 <= 9)
