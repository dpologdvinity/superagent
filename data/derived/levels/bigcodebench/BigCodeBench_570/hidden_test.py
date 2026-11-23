from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json
class TestCases(unittest.TestCase):
    def test_regular_function(self):
        def sample_function(x, y, z=3): pass
        result = json.loads(task_func(sample_function))
        self.assertEqual(result['function_name'], 'sample_function')
        self.assertIn('y', result['args'])
    def test_lambda_function(self):
        lambda_func = lambda x, y=2: x + y
        result = json.loads(task_func(lambda_func))
        self.assertTrue(result['is_lambda'])
        self.assertEqual(result['function_name'], '<lambda>')
    def test_no_arguments(self):
        def no_arg_func(): pass
        result = json.loads(task_func(no_arg_func))
        self.assertEqual(len(result['args']), 0)
    def test_function_with_no_defaults(self):
        def func_no_defaults(x, y): pass
        result = json.loads(task_func(func_no_defaults))
        self.assertIsNone(result['defaults'])
    def test_function_name(self):
        def simple_function(): pass
        result = json.loads(task_func(simple_function))
        self.assertEqual(result['function_name'], 'simple_function')
    
    def test_function_annotations(self):
        def annotated_function(x: int, y: str = 'hello') -> None: pass
        result = json.loads(task_func(annotated_function))
        self.assertDictEqual(result['annotations'], {'x': 'int', 'y': 'str', 'return': 'None'})
