from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = task_func('Python is great. I love Python.', 2)
        expected = [('Python', 2), ('is', 1)]
        self.assertEqual(result, expected)

    def test_case_2(self):
        result = task_func('Visit https://www.python.org for more info. Python is great. I love Python.', 2)
        expected = [('Python', 2), ('Visit', 1)]
        self.assertEqual(result, expected)

    def test_case_3(self):
        text = 'Visit https://www.python.org and http://www.example.com. Python é ótimo! Adoro Python!'
        result = task_func(text, 2)
        expected = [('Python', 2), ('Visit', 1)]
        self.assertEqual(result, expected)
