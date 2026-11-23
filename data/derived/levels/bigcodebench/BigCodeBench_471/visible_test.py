from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_data = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana']
        expected_output = pd.DataFrame({'Count': [2, 3, 1]}, index=['apple', 'banana', 'cherry'])
        pd.testing.assert_frame_equal(task_func(input_data), expected_output)

    def test_case_2(self):
        input_data = ['apple', 'apple', 'apple']
        expected_output = pd.DataFrame({'Count': [3]}, index=['apple'])
        pd.testing.assert_frame_equal(task_func(input_data), expected_output)

    def test_case_3(self):
        input_data = []
        expected_output = pd.DataFrame(columns=['Count'])
        pd.testing.assert_frame_equal(task_func(input_data), expected_output)
