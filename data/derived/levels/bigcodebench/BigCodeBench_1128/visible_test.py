from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import json
import hashlib
import base64
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path_1 = os.path.join(self.temp_dir, 'test1.json')
        self.path_2 = os.path.join(self.temp_dir, 'test2.json')
        sample_data_1 = {'A': {'B': {'maindata': [{'Info': 'hello world'}]}, 'C': {'maindata': [{'Info': 'goodbye world'}]}}}
        sample_data_2 = {'A': {'D': {'maindata': [{'Info': 'another world'}]}, 'E': {'maindata': [{'Info': 'yet another world'}]}}}
        with open(self.path_1, 'w') as f:
            json.dump(sample_data_1, f)
        with open(self.path_2, 'w') as f:
            json.dump(sample_data_2, f)

    def tearDown(self):
        os.remove(self.path_1)
        os.remove(self.path_2)
        os.rmdir(self.temp_dir)

    def test_hash_length_for_key_B(self):
        result = task_func(self.path_1, 'B')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)

    def test_hash_length_for_key_C(self):
        result = task_func(self.path_1, 'C')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)

    def test_hash_length_for_key_D(self):
        result = task_func(self.path_2, 'D')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)
