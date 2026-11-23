from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        json_str = '{"name": "John", "website": "qwerthttps://www.example.com"}'
        result = task_func(json_str)
        self.assertEqual(result, {})

    def test_case_2(self):
        json_str = '{"name": "John", "social": {"twitter": "https://twitter.com/john", "linkedin": "https://linkedin.com/in/john"}, "website": "https://linkedin.com/in/john"}'
        result = task_func(json_str)
        self.assertEqual(result, {'https://twitter.com/john': 1, 'https://linkedin.com/in/john': 2})
        result = task_func(json_str, 1)
        self.assertEqual(result, {'https://linkedin.com/in/john': 2})

    def test_case_3(self):
        json_str = 'This is an adversarial input 0061'
        with self.assertRaises(json.decoder.JSONDecodeError):
            result = task_func(json_str)
