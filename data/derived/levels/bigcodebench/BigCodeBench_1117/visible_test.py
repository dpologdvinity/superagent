from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import collections
import random
import json
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

class TestCases(unittest.TestCase):

    def test_case_1(self):
        random.seed(0)
        input_data = {'EMP$$': 5, 'MAN$$': 3, 'DEV$$': 4, 'HR$$': 2}
        output_data = task_func(input_data)
        parsed_output = json.loads(output_data)
        for key, value in input_data.items():
            self.assertIn(key, parsed_output)
            self.assertEqual(len(parsed_output[key]), value)
            for level in parsed_output[key]:
                self.assertIn(level, LEVELS)

    def test_case_2(self):
        random.seed(0)
        input_data = {'EMP$$': 10}
        output_data = task_func(input_data)
        parsed_output = json.loads(output_data)
        self.assertEqual(len(parsed_output), 1)
        self.assertEqual(len(parsed_output['EMP$$']), 10)
        for level in parsed_output['EMP$$']:
            self.assertIn(level, LEVELS)

    def test_case_3(self):
        random.seed(0)
        input_data = {'MAN$$': 6, 'DEV$$': 7}
        output_data = task_func(input_data)
        parsed_output = json.loads(output_data)
        self.assertEqual(len(parsed_output), 2)
        self.assertEqual(len(parsed_output['MAN$$']), 6)
        self.assertEqual(len(parsed_output['DEV$$']), 7)
        for level in parsed_output['MAN$$']:
            self.assertIn(level, LEVELS)
        for level in parsed_output['DEV$$']:
            self.assertIn(level, LEVELS)
