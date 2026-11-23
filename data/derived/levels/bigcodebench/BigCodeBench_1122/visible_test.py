from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_str = 'Visit http://www.google.com for more details.'
        with patch('socket.gethostbyname', return_value='192.0.2.1'):
            result = task_func(input_str)
            self.assertEqual(result, {'www.google.com': '192.0.2.1'})

    def test_case_2(self):
        input_str = 'Check these links: http://www.google.com, https://www.python.org'
        with patch('socket.gethostbyname', side_effect=['192.0.2.1', '192.0.2.2']):
            result = task_func(input_str)
            self.assertEqual(result, {'www.google.com': '192.0.2.1', 'www.python.org': '192.0.2.2'})

    def test_case_3(self):
        input_str = 'Hello, World!'
        result = task_func(input_str)
        self.assertEqual(result, {})
