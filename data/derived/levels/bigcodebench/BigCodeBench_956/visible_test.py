from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = task_func('Hello   World!', seed=1)
        self.assertNotIn(' ', result, 'Spaces should be replaced.')
        self.assertNotIn('!', result, 'Special characters should be removed.')
        self.assertEqual(len(result), len('Hello___World'), 'Length should match processed input.')

    def test_case_2(self):
        result = task_func('Python!', seed=2)
        self.assertNotIn('!', result, 'Special characters should be removed.')
        self.assertEqual(len(result), len('Python'), 'Length should match processed input.')

    def test_case_3(self):
        result = task_func('  ', seed=3)
        self.assertEqual(result, '__', 'Spaces should be replaced with underscores.')
