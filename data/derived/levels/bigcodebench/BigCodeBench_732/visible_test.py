from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = task_func('running runner run')
        self.assertEqual(result, {'run': 1, 'runner': 1})

    def test_case_2(self):
        result = task_func('dancing dancer danced')
        self.assertEqual(result, {'danc': 1, 'dancer': 1})

    def test_case_3(self):
        result = task_func('loving lover love')
        self.assertEqual(result, {'love': 1, 'lover': 1})
