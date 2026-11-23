from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
import doctest
import tempfile
# Define the TestCases class containing the blackbox test cases
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup function to create a test directory before each test case
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_directory = f"{self.base_tmp_dir}/test"
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)
        os.mkdir(self.test_directory)
    def tearDown(self):
        # Teardown function to remove the test directory after each test case
        shutil.rmtree(self.test_directory)
    def create_sample_files(self, file_list):
        # Helper function to create sample files for test cases
        for file in file_list:
            with open(os.path.join(self.test_directory, file), "w") as f:
                f.write(f"Content of {file}")
    def test_case_1(self):
        # Test case 1: Organizing files with standard extensions
        files = ["file1.txt", "image1.jpg", "document1.pdf"]
        self.create_sample_files(files)
        
        task_func(self.test_directory)
        
        expected_directories = ["txt", "jpg", "pdf"]
        actual_directories = os.listdir(self.test_directory)
        
        for dir_name in expected_directories:
            self.assertIn(dir_name, actual_directories)
    def test_case_2(self):
        # Test case 2: Organizing files with no extensions
        files = ["file1", "document2"]
        self.create_sample_files(files)
        
        task_func(self.test_directory)
        
        # Expected behavior: files without extensions remain in the main directory
        for file_name in files:
            self.assertIn(file_name, os.listdir(self.test_directory))
    def test_case_3(self):
        # Test case 3: Organizing files with uncommon or made-up extensions
        files = ["data.xyz", "notes.abc123"]
        self.create_sample_files(files)
        
        task_func(self.test_directory)
        
        expected_directories = ["xyz", "abc123"]
        actual_directories = os.listdir(self.test_directory)
        
        for dir_name in expected_directories:
            self.assertIn(dir_name, actual_directories)
    def test_case_4(self):
        # Test case 4: Checking the behavior when the directory is empty
        task_func(self.test_directory)
        
        # Expected behavior: directory remains empty
        self.assertEqual(len(os.listdir(self.test_directory)), 0)
    def test_case_5(self):
        # Test case 5: Checking the behavior when some sub-directories already exist
        os.mkdir(os.path.join(self.test_directory, "txt"))
        files = ["file1.txt", "file2.txt"]
        self.create_sample_files(files)
        
        task_func(self.test_directory)
        
        # Expected behavior: files are moved to the existing "txt" sub-directory
        txt_files = os.listdir(os.path.join(self.test_directory, "txt"))
        for file_name in files:
            self.assertIn(file_name, txt_files)
