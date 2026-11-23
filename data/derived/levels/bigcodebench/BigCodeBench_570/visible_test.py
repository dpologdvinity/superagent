from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json

class TestCases(unittest.TestCase):

    def test_regular_function(self):

        def sample_function(x, y, z=3):
            pass
        result = json.loads(task_func(sample_function))
        self.assertEqual(result['function_name'], 'sample_function')
        self.assertIn('y', result['args'])

    def test_lambda_function(self):
        lambda_func = lambda x, y=2: x + y
        result = json.loads(task_func(lambda_func))
        self.assertTrue(result['is_lambda'])
        self.assertEqual(result['function_name'], '<lambda>')

    def test_no_arguments(self):

        def no_arg_func():
            pass
        result = json.loads(task_func(no_arg_func))
        self.assertEqual(len(result['args']), 0)
