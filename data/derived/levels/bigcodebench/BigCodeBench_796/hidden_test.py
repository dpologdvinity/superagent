from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
from pathlib import Path
import shutil
class TestCases(unittest.TestCase):
    # Function to create the mock directory structure and files
    def create_test_files(self, base_path, file_dict):
        for name, content in file_dict.items():
            path = Path(base_path) / name
            if isinstance(content, dict):  # it's a directory
                path.mkdir()
                self.create_test_files(path, content)
            else:  # it's a file
                path.write_text(content)
    # Define a directory structure with files containing brackets and without brackets
    test_files = {
        'file1.txt': '',  # without brackets
        'file(2).txt': '',  # with round brackets
        'file[3].png': '',  # with square brackets
        'file{4}.jpg': '',  # with curly brackets
        'folder1': {
            'file(5).jpg': '',  # with round brackets
            'file6.csv': '',  # without brackets
            'folder2': {
                'file[7].csv': '',  # with square brackets
                'file{8}.png': ''  # with curly brackets
            }
        }
    }
# Create a temporary directory structure for testing
    temp_dir = ''
    def setUp(self):
        self.temp_dir = os.path.join(os.getcwd(), 'temp_test_dir')
        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)
        self.create_test_files(self.temp_dir, self.test_files)
    
    def test_case_1(self):
        # Test with the root directory
        result = task_func(self.temp_dir)
        self.assertIn(os.path.join(self.temp_dir, 'file(2).txt'), result)
        self.assertIn(os.path.join(self.temp_dir, 'file[3].png'), result)
        self.assertIn(os.path.join(self.temp_dir, 'file{4}.jpg'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'file(5).jpg'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file[7].csv'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file{8}.png'), result)
        self.assertEqual(len(result), 6)
        
    def test_case_2(self):
        # Test with a sub-directory
        result = task_func(os.path.join(self.temp_dir, 'folder1'))
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'file(5).jpg'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file[7].csv'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file{8}.png'), result)
        self.assertEqual(len(result), 3)
        
    def test_case_3(self):
        # Test with a deeper sub-directory
        result = task_func(os.path.join(self.temp_dir, 'folder1', 'folder2'))
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file[7].csv'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file{8}.png'), result)
        self.assertEqual(len(result), 2)
    def test_case_4(self):
        # Test with an empty directory
        empty_dir = os.path.join(self.temp_dir, 'empty_folder')
        os.mkdir(empty_dir)
        result = task_func(empty_dir)
        self.assertEqual(result, [])
    def test_case_5(self):
        # Test with directory containing files without brackets
        no_bracket_dir = os.path.join(self.temp_dir, 'no_bracket_folder')
        os.mkdir(no_bracket_dir)
        open(os.path.join(no_bracket_dir, 'file9.txt'), 'w').close()
        open(os.path.join(no_bracket_dir, 'file10.jpg'), 'w').close()
        result = task_func(no_bracket_dir)
        self.assertEqual(result, [])
    def tearDown(self):
        shutil.rmtree('temp_test_dir')
