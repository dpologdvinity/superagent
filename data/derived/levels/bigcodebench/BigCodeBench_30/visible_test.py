from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import json
import os
import re
EMAIL_REGEX = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)'

class TestCases(unittest.TestCase):

    def setUp(self):
        self.filepath = '/tmp/test_data.json'
        self.valid_data = {'name': 'John Doe', 'age': 30, 'email': 'john.doe@example.com'}
        self.invalid_email_data = {'name': 'John Doe', 'age': 30, 'email': 'johndoe@example'}
        with open(self.filepath, 'w') as file:
            json.dump(self.valid_data, file)

    def tearDown(self):
        os.remove(self.filepath)

    def test_case_valid_json(self):
        result = task_func(self.filepath, 'name')
        self.assertEqual(result, 'John Doe')

    def test_case_invalid_email_format(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.invalid_email_data, file)
        with self.assertRaises(ValueError):
            task_func(self.filepath, 'email')

    def test_case_missing_attribute(self):
        modified_data = self.valid_data.copy()
        del modified_data['age']
        with open(self.filepath, 'w') as file:
            json.dump(modified_data, file)
        with self.assertRaises(ValueError):
            task_func(self.filepath, 'age')
