from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_enum_serialization(self):
        obj = {'color': Color.RED}
        result = task_func(obj)
        self.assertIn('"color": "RED"', result)

    def test_multiple_enum_serialization(self):
        obj = {'colors': [Color.RED, Color.GREEN, Color.BLUE]}
        result = task_func(obj)
        self.assertIn('"colors": ["RED", "GREEN", "BLUE"]', result)

    def test_no_enum_serialization(self):
        obj = {'name': 'Bob', 'age': 25}
        result = task_func(obj)
        self.assertEqual(result, '{"name": "Bob", "age": 25}')
