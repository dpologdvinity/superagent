from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_repeating_pairs(self):
        self.assertEqual(task_func('aabbcc'), [('aa', 1)], 'Should identify single repeating pair')

    def test_mixed_repeating_pairs(self):
        self.assertEqual(task_func('abcabc'), [('ab', 2)], 'Should identify most frequent pair in mixed sequence')

    def test_single_character(self):
        self.assertEqual(task_func('a'), [], 'Should return empty list for single character')
