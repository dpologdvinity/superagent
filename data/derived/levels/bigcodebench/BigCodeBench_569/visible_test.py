from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import math

class TestCases(unittest.TestCase):

    def test_regular_function(self):

        def sample_function(x, y, z=3):
            pass
        result = task_func(sample_function)
        self.assertEqual(result['function_name'], 'sample_function')
        self.assertEqual(result['sqrt_args'], math.sqrt(3))

    def test_lambda_in_defaults(self):

        def func_with_lambda(x, y=lambda a: a + 2):
            pass
        result = task_func(func_with_lambda)
        self.assertEqual(result['lambda_in_defaults'], 1)

    def test_no_arguments(self):

        def no_arg_func():
            pass
        result = task_func(no_arg_func)
        self.assertEqual(result['sqrt_args'], 0)
