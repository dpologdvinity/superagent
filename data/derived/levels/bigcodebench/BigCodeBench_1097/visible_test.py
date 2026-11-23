from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_text = 'Visit https://www.python.org for more info. I love to eat apples and oranges!'
        expected_output = 'Visit info love eat apples oranges'
        result = task_func(input_text)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        input_text = 'Check out https://www.google.com and also https://www.openai.com'
        expected_output = 'Check also'
        result = task_func(input_text)
        self.assertEqual(result, expected_output)

    def test_case_3(self):
        input_text = 'Hello, world! How are you today?'
        expected_output = 'Hello world How today'
        result = task_func(input_text)
        self.assertEqual(result, expected_output)
