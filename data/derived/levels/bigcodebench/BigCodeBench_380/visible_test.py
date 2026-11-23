from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
import doctest
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_directory = f'{self.base_tmp_dir}/test'
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)
        os.mkdir(self.test_directory)

    def tearDown(self):
        shutil.rmtree(self.test_directory)

    def create_sample_files(self, file_list):
        for file in file_list:
            with open(os.path.join(self.test_directory, file), 'w') as f:
                f.write(f'Content of {file}')

    def test_case_1(self):
        files = ['file1.txt', 'image1.jpg', 'document1.pdf']
        self.create_sample_files(files)
        task_func(self.test_directory)
        expected_directories = ['txt', 'jpg', 'pdf']
        actual_directories = os.listdir(self.test_directory)
        for dir_name in expected_directories:
            self.assertIn(dir_name, actual_directories)

    def test_case_2(self):
        files = ['file1', 'document2']
        self.create_sample_files(files)
        task_func(self.test_directory)
        for file_name in files:
            self.assertIn(file_name, os.listdir(self.test_directory))

    def test_case_3(self):
        files = ['data.xyz', 'notes.abc123']
        self.create_sample_files(files)
        task_func(self.test_directory)
        expected_directories = ['xyz', 'abc123']
        actual_directories = os.listdir(self.test_directory)
        for dir_name in expected_directories:
            self.assertIn(dir_name, actual_directories)
