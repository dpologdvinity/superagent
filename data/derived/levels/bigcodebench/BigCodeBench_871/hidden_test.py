from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        # Variables for the tests
        self.data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        self.file_name = "test_output.txt"
    def tearDown(self) -> None:
        if os.path.isfile(self.file_name):
            os.remove(self.file_name)
    def read_file_content(self, file_path):
        # Read the content of the file and return it as a list of lines
        with open(file_path, 'r') as file:
            return file.readlines()
    def test_mean_values_with_valid_data(self):
        expected_means = [3.0, 4.0]  # Expected mean values
        expected_file_content = ["Position 1: 3.0\n", "Position 2: 4.0\n"]
        result = task_func(self.data_list, self.file_name)
        self.assertEqual(result, expected_means)
        self.assertTrue(os.path.isfile(self.file_name))  # Check file creation
        # Verify the content of the created file
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)
    def test_function_with_empty_data(self):
        result = task_func([], self.file_name)
        self.assertEqual(result, [])  # Should return an empty list
        self.assertTrue(os.path.isfile(self.file_name))  # Check file creation
        expected_file_content = []
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)
    def test_function_with_non_numeric_data(self):
        data_with_non_numeric = [('a', 'x', 'y'), ('b', 'p', 'q')]
        result = task_func(data_with_non_numeric, self.file_name)
        self.assertEqual(result, [np.nan, np.nan])
        self.assertTrue(os.path.isfile(self.file_name))  # Check file creation
        expected_file_content = ["Position 1: nan\n", "Position 2: nan\n"]
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)
    def test_function_with_incomplete_tuples(self):
        inconsistent_data = [('a', 1), ('b',), ('c', 2, 3)]
        expected_means = [1.5, 3.0]  # Expected means
        result = task_func(inconsistent_data, self.file_name)
        self.assertEqual(result, expected_means)
        self.assertTrue(os.path.isfile(self.file_name))  # Check file creation
        expected_file_content = ["Position 1: 1.5\n", "Position 2: 3.0\n"]
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)
    def test_function_with_all_nan_values(self):
        data_all_nan = [('a', np.nan, np.nan) for _ in range(5)]
        expected_means = [np.nan, np.nan]
        result = task_func(data_all_nan, self.file_name)
        # Check if all values are 'nan'
        self.assertTrue(result, expected_means)
        self.assertTrue(os.path.isfile(self.file_name))  # Check file creation
        expected_file_content = ["Position 1: nan\n", "Position 2: nan\n"]
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)
