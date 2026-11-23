from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(task_func([]), {'x': None, 'y': None, 'z': None})

    def test_valid_input(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        result = task_func(data)
        self.assertAlmostEqual(result['x']['mean'], 2.0)
        self.assertAlmostEqual(result['y']['mean'], 8.666666666666666)
        self.assertAlmostEqual(result['z']['mean'], 6.0)

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            task_func('not a list')
