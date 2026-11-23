from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
import time
from unittest.mock import patch

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = 'task_func_test_dir'
        os.makedirs(self.temp_dir, exist_ok=True)
        self.r_script_path = os.path.join(self.temp_dir, 'mock_script.r')
        with open(self.r_script_path, 'w') as file:
            file.write('write.csv(data.frame(x=1:10, y=11:20), "{}/output.csv")')
        self.output_path = self.temp_dir

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    @patch('subprocess.call', return_value=None)
    def test_case_1(self, mock_subprocess_call):
        with open(os.path.join(self.output_path, 'output.csv'), 'w') as file:
            file.write('x,y\n1,11\n2,12\n3,13\n4,14\n5,15\n6,16\n7,17\n8,18\n9,19\n10,20')
        result, message = task_func(self.r_script_path, self.output_path, 5)
        self.assertTrue(result)
        self.assertEqual(message, 'File generated successfully within the specified duration.')

    @patch('subprocess.call', return_value=None)
    def test_case_2(self, mock_subprocess_call):
        result, message = task_func(self.r_script_path, self.output_path, 0)
        self.assertFalse(result)
        self.assertEqual(message, 'File not generated within the specified duration.')

    @patch('subprocess.call', return_value=None)
    def test_case_3(self, mock_subprocess_call):
        invalid_path = 'invalid/path/mock_script.r'
        result, message = task_func(invalid_path, self.output_path, 5)
        self.assertFalse(result)
        self.assertEqual(message, 'File not generated within the specified duration.')
