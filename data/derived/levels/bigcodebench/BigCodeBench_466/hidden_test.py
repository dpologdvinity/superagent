from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_enum_serialization(self):
        # Test serialization of a dictionary containing an Enum to check if the Enum is properly converted to its name.
        obj = {'color': Color.RED}
        result = task_func(obj)
        self.assertIn('"color": "RED"', result)
    def test_multiple_enum_serialization(self):
        # Test serialization of a dictionary with a list of Enums to verify if all Enums are correctly serialized by their names.
        obj = {'colors': [Color.RED, Color.GREEN, Color.BLUE]}
        result = task_func(obj)
        self.assertIn('"colors": ["RED", "GREEN", "BLUE"]', result)
    def test_no_enum_serialization(self):
        # Test serialization of a simple dictionary without Enums to ensure basic JSON serialization functionality is unaffected.
        obj = {'name': 'Bob', 'age': 25}
        result = task_func(obj)
        self.assertEqual(result, '{"name": "Bob", "age": 25}')
    def test_nested_enum_serialization(self):
        # Test serialization of a nested dictionary containing an Enum to ensure deep serialization handles Enums correctly.
        obj = {'person': {'name': 'Alice', 'favorite_color': Color.BLUE}}
        result = task_func(obj)
        self.assertIn('"favorite_color": "BLUE"', result)
    def test_empty_object_serialization(self):
        # Test serialization of an empty dictionary to verify the encoder handles empty objects correctly.
        obj = {}
        result = task_func(obj)
        self.assertEqual(result, '{}')
    def test_direct_enum_serialization(self):
        # Test direct serialization of an Enum instance
        result = task_func(Color.GREEN)
        self.assertEqual(result, '"GREEN"')
    def test_complex_nested_structures(self):
        # Test serialization of complex nested structures including Enum
        obj = {'people': [{'name': 'Alice', 'favorite_color': Color.BLUE}, {'name': 'Bob', 'favorite_color': Color.RED}]}
        result = task_func(obj)
        self.assertIn('"favorite_color": "BLUE"', result)
        self.assertIn('"favorite_color": "RED"', result)
