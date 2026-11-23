from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_texts = ['Visit https://www.python.org for more info.', 'Python is great.', 'I love Python.']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_2(self):
        input_texts = ['Hello world!', 'Python programming is fun.', 'Data science with Python.']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_3(self):
        input_texts = ['I love coding.', 'You love coding too.', 'We all love coding.']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_4(self):
        input_texts = ['Check out this amazing article at https://www.example.com/article']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_5(self):
        input_texts = ['', '', '']
        expected_output = ([], [])
        self.assertEqual(task_func(input_texts), expected_output)
