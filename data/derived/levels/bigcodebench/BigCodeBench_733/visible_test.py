from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(task_func('this is an example content'), 1)

    def test_case_2(self):
        self.assertEqual(task_func('this is an the of'), 0)

    def test_case_3(self):
        self.assertEqual(task_func('example content programming'), 2)
