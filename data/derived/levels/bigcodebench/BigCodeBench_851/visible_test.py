from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_str = 'Hello world\nThis is a test string\nHappy coding!'
        width = 10
        expected_output = 'Hello\nworld This\nwas a test\nstring\nHappy\ncoding!'
        self.assertEqual(task_func(input_str, width), expected_output)

    def test_case_2(self):
        input_str = 'Hello world'
        width = 5
        expected_output = 'Hello\nworld'
        self.assertEqual(task_func(input_str, width), expected_output)

    def test_case_3(self):
        input_str = ''
        width = 10
        expected_output = ''
        self.assertEqual(task_func(input_str, width), expected_output)
