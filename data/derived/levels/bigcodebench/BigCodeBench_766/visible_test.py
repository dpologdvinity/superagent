from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_empty_pattern(self):
        """empty pattern"""
        result = task_func('asdf', patterns=[])
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_wrong_type(self):
        """wrong input types"""
        self.assertRaises(Exception, task_func, {'string': 123})
        self.assertRaises(Exception, task_func, {'string': ['asdf']})
        self.assertRaises(Exception, task_func, {'string': {'a': 3}})
        self.assertRaises(Exception, task_func, {'string': ['test'], 'patterns': 3})
        self.assertRaises(Exception, task_func, {'string': ['test'], 'patterns': ['3', 1]})

    def test_case_1(self):
        result = task_func('nnnaaaasssdddeeefffggg')
        expected_result = {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
        self.assertEqual(result, expected_result)
