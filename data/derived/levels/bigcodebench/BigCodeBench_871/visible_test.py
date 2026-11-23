from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import numpy as np

class TestCases(unittest.TestCase):

    def setUp(self):
        self.data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        self.file_name = 'test_output.txt'

    def tearDown(self) -> None:
        if os.path.isfile(self.file_name):
            os.remove(self.file_name)

    def read_file_content(self, file_path):
        with open(file_path, 'r') as file:
            return file.readlines()

    def test_mean_values_with_valid_data(self):
        expected_means = [3.0, 4.0]
        expected_file_content = ['Position 1: 3.0\n', 'Position 2: 4.0\n']
        result = task_func(self.data_list, self.file_name)
        self.assertEqual(result, expected_means)
        self.assertTrue(os.path.isfile(self.file_name))
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)

    def test_function_with_empty_data(self):
        result = task_func([], self.file_name)
        self.assertEqual(result, [])
        self.assertTrue(os.path.isfile(self.file_name))
        expected_file_content = []
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)

    def test_function_with_non_numeric_data(self):
        data_with_non_numeric = [('a', 'x', 'y'), ('b', 'p', 'q')]
        result = task_func(data_with_non_numeric, self.file_name)
        self.assertEqual(result, [np.nan, np.nan])
        self.assertTrue(os.path.isfile(self.file_name))
        expected_file_content = ['Position 1: nan\n', 'Position 2: nan\n']
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)
