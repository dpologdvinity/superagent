from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = [{'hi': 7, 'bye': 4, 'http://google.com': 0}, {'https://google.com': 0}, {'http://www.cwi.nl': 1}]
        expected_output = {0: 2}
        self.assertEqual(task_func(result), expected_output)

    def test_case_2(self):
        result = [{'http://google.com': 2}, {'http://www.cwi.nl': 2}, {'http://google.com': 3}]
        expected_output = {2: 2}
        self.assertEqual(task_func(result), expected_output)

    def test_case_3(self):
        result = [{'http://google.com': 5}]
        expected_output = {5: 1}
        self.assertEqual(task_func(result), expected_output)
