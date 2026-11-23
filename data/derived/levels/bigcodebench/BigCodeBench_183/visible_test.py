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
        input_data = json.dumps({'key': 'value'})
        response = task_func(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)

    def test_case_2(self):
        input_data = json.dumps({})
        response = task_func(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)

    def test_case_3(self):
        input_data = json.dumps({'users': [{'name': 'John', 'age': 30}, {'name': 'Doe', 'age': 25}]})
        response = task_func(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
