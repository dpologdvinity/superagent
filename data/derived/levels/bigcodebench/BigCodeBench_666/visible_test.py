from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def base(self, seq, letter_weight_dict, correct_seq):
        result = task_func(seq, letter_weight_dict)
        self.assertTrue(isinstance(result, str))
        self.assertEqual(result, correct_seq)

    def test_case_1(self):
        self.base('abc', {'a': 1, 'b': 2, 'c': 3}, 'abc')

    def test_case_2(self):
        self.base('aabc', {'a': 10, 'b': -5, 'c': 3}, 'aac')

    def test_case_3(self):
        self.base('zx', {'x': 1, 'z': 2}, 'zx')
