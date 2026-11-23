from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import doctest
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file_path = f'{self.temp_dir}/test_log.json'

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_case_1(self):
        result_path = task_func(self.test_file_path, 5, seed=42)
        self.assertEqual(result_path, self.test_file_path)
        self.assertTrue(os.path.exists(result_path))
        with open(result_path, 'r') as json_file:
            data = json.load(json_file)
            self.assertEqual(len(data), 5)

    def test_case_2(self):
        result_path = task_func(self.test_file_path, 100, seed=42)
        self.assertEqual(result_path, self.test_file_path)
        self.assertTrue(os.path.exists(result_path))
        with open(result_path, 'r') as json_file:
            data = json.load(json_file)
            self.assertEqual(len(data), 100)

    def test_case_3(self):
        result_path = task_func(self.test_file_path, 10, seed=42)
        with open(result_path, 'r') as json_file:
            data1 = json.load(json_file)
        os.remove(result_path)
        result_path = task_func(self.test_file_path, 10, seed=42)
        with open(result_path, 'r') as json_file:
            data2 = json.load(json_file)
        self.assertEqual(data1, data2)
