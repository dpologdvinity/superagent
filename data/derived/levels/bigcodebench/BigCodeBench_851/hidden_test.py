from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        input_str = "Hello world\nThis is a test string\nHappy coding!"
        width = 10
        expected_output = "Hello\nworld This\nwas a test\nstring\nHappy\ncoding!"
        self.assertEqual(task_func(input_str, width), expected_output)
        
        
    def test_case_2(self):
        # Test with single line and specific width
        input_str = "Hello world"
        width = 5
        expected_output = "Hello\nworld"
        self.assertEqual(task_func(input_str, width), expected_output)
    
    def test_case_3(self):
        # Test with empty string and specific width
        input_str = ""
        width = 10
        expected_output = ""
        self.assertEqual(task_func(input_str, width), expected_output)
    
    def test_case_4(self):
        input_str = "Hello world This is a test string Happy coding!"
        width = 1000
        expected_output = "Hello world This was a test string Happy coding!"  # Very wide width, should not wrap
        self.assertEqual(task_func(input_str, width), expected_output)
    
    def test_case_5(self):
        # Test with special characters and specific width
        input_str = "Hello, @world!\n#This$is^a&test*string"
        width = 10
        expected_output = "Hello,\n@world!\n#This$was^a&test*string"
        self.assertEqual(task_func(input_str, width), expected_output)
