from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json
from django.conf import settings
if not settings.configured:
    settings.configure(DEBUG=True)
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Testing with a simple JSON data
        input_data = json.dumps({"key": "value"})
        response = task_func(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
        
    def test_case_2(self):
        # Testing with an empty JSON data
        input_data = json.dumps({})
        response = task_func(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
        
    def test_case_3(self):
        # Testing with a more complex JSON data
        input_data = json.dumps({"users": [{"name": "John", "age": 30}, {"name": "Doe", "age": 25}]})
        response = task_func(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
    def test_case_4(self):
        # Testing with JSON data containing special characters
        input_data = json.dumps({"description": "This is a sample data with special characters: !@#%^&*()_-+={[]}"})
        response = task_func(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
    def test_case_5(self):
        # Testing with JSON data containing numeric values
        input_data = json.dumps({"numbers": [1, 2, 3, 4, 5]})
        response = task_func(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
