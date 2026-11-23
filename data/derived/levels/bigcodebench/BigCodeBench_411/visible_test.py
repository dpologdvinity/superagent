from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import json
import os

class TestCases(unittest.TestCase):

    def read_json_file(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def tearDown(self):
        files_to_remove = ['./default_data_output.json', './custom_data_output_2.json', './custom_data_output_3.json', './custom_data_output_4.json', './custom_data_output_5.json']
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)

    def convert_keys_to_str(self, dictionary):
        if not isinstance(dictionary, dict):
            return dictionary
        return {str(k): self.convert_keys_to_str(v) for k, v in dictionary.items()}

    def test_case_1(self):
        data = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        df = pd.DataFrame(data)
        output_path = task_func(data)
        self.assertTrue(os.path.exists(output_path))
        expected_data = self.convert_keys_to_str(df.drop(columns='c').to_dict(orient='dict'))
        self.assertEqual(self.read_json_file(output_path), expected_data)

    def test_case_2(self):
        data = {'name': ['Alice', 'Bob'], 'country': ['USA', 'Canada'], 'c': ['x', 'y']}
        df = pd.DataFrame(data)
        custom_path = './custom_data_output_2.json'
        output_path = task_func(data, custom_path)
        self.assertTrue(os.path.exists(output_path))
        expected_data = self.convert_keys_to_str(df.drop(columns='c').to_dict(orient='dict'))
        self.assertEqual(self.read_json_file(output_path), expected_data)

    def test_case_3(self):
        data = {'age': [25, 30], 'height': [170, 175]}
        df = pd.DataFrame(data)
        custom_path = './custom_data_output_3.json'
        output_path = task_func(data, custom_path)
        self.assertTrue(os.path.exists(output_path))
        expected_data = self.convert_keys_to_str(df.to_dict(orient='dict'))
        self.assertEqual(self.read_json_file(output_path), expected_data)
