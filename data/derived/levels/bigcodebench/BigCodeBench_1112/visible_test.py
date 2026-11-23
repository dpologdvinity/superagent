from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import csv
import random

class TestCases(unittest.TestCase):

    def setUp(self):
        self.mock_file_name = 'test_task_func_data.csv'

    def tearDown(self):
        if os.path.exists(self.mock_file_name):
            os.remove(self.mock_file_name)

    def test_case_1(self):
        random.seed(0)
        returned_file = task_func(self.mock_file_name)
        self.assertTrue(os.path.exists(returned_file))

    def test_case_2(self):
        random.seed(0)
        returned_file = task_func(self.mock_file_name)
        self.assertTrue(os.path.exists(returned_file))

    def test_case_3(self):
        random.seed(0)
        task_func(self.mock_file_name)
        with open(self.mock_file_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertEqual(header, ['Time', 'Temperature', 'Humidity', 'Pressure'])
