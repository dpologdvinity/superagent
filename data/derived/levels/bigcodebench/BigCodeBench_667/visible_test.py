from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(task_func({'a': 1, 'b': 2, 'c': 3}, 2), ['c', 'b'])

    def test_case_2(self):
        self.assertEqual(task_func({'a': 1, 'b': 2, 'c': 3}, 1), ['c'])

    def test_case_3(self):
        self.assertEqual(task_func({'a': 1, 'b': 2, 'c': 3}, 3), ['c', 'b', 'a'])
