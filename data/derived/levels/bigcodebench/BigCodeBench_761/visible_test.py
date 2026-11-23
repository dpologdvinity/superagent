from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json
from collections import Counter

class TestCases(unittest.TestCase):

    def test_basic(self):
        json_str = '{"name": "John", "age": null, "email": "john@example.com"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1, 'None': 1})}
        self.assertEqual(result, expected)

    def test_multiple_none(self):
        json_str = '{"name": "John", "age": null, "city": null, "email": "john@example.com"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1, 'None': 1})}
        self.assertEqual(result, expected)

    def test_multiple_emails(self):
        json_str = '{"name": "John", "email1": "john1@example.com", "email2": "john2@example.com"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'email1': 'None', 'email2': 'None'}, 'value_counts': Counter({'None': 2, 'John': 1})}
        self.assertEqual(result, expected)
