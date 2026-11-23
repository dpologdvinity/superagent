from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(task_func([[5.1, 5.0, 1.4], [4.9, 4.8, 1.4], [4.7, 4.6, 2.0]], ['x', 'y', 'z'], 0.9), [('x', 'y')])

    def test_case_2(self):
        self.assertEqual(task_func([[5.1, 5.0, 1.4], [4.9, 4.8, 1.4], [4.7, 4.6, 2.0]], ['x', 'y', 'z'], 0.5), [('x', 'y'), ('x', 'z'), ('y', 'z')])

    def test_case_3(self):
        self.assertEqual(task_func([[5.1, 5.0, 1.4], [4.9, 4.8, 1.4], [4.7, 4.6, 2.0]], ['x', 'y', 'z'], 0.1), [('x', 'y'), ('x', 'z'), ('y', 'z')])
