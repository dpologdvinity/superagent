from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        """Checks the basic functionality with single-element lists."""
        input_dict = {'a': [1], 'b': [2], 'c': [3]}
        expected_output = {1: 1, 2: 1, 3: 1}
        self.assertEqual(task_func(input_dict), expected_output)

    def test_case_2(self):
        """Verifies the function with lists that have distinct integers."""
        input_dict = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        expected_output = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
        self.assertEqual(task_func(input_dict), expected_output)

    def test_case_3(self):
        """ Tests the function with lists containing duplicate integers to ensure counts are aggregated correctly."""
        input_dict = {'a': [1, 1, 2], 'b': [3, 4, 4], 'c': [5, 5, 5]}
        expected_output = {1: 2, 2: 1, 3: 1, 4: 2, 5: 3}
        self.assertEqual(task_func(input_dict), expected_output)
