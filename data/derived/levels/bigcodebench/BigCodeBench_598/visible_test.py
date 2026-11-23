from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elephant', 'fig', 'grape', 'kiwi']}
        result = task_func(df, 'a')
        expected_result = {5: 1}
        self.assertDictEqual(result, expected_result)

    def test_case_2(self):
        df = {'Word': ['cat', 'dog', 'elephant', 'fish', 'goose']}
        result = task_func(df, 'e')
        expected_result = {8: 1}
        self.assertDictEqual(result, expected_result)

    def test_case_3(self):
        df = {'Word': ['kiwi', 'lemon', 'mango', 'nectarine', 'orange']}
        result = task_func(df, 'm')
        expected_result = {5: 1}
        self.assertDictEqual(result, expected_result)
