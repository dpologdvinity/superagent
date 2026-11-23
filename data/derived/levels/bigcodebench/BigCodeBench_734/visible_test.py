from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import re

class TestCases(unittest.TestCase):

    def test_case_1(self):
        sentence = 'this is an example content'
        expected_output = {'DT': 2, 'NN': 1, 'VBZ': 1}
        self.assertEqual(task_func(sentence), expected_output)

    def test_case_2(self):
        sentence = 'The quick brown fox jumps'
        expected_output = {'DT': 1, 'JJ': 1, 'NN': 2}
        self.assertEqual(task_func(sentence), expected_output)

    def test_case_3(self):
        sentence = 'Over the lazy dog'
        expected_output = {'DT': 1, 'IN': 1, 'NN': 1}
        self.assertEqual(task_func(sentence), expected_output)
