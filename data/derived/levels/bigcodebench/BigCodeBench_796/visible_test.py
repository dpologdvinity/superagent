from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
from pathlib import Path
import shutil

class TestCases(unittest.TestCase):

    def create_test_files(self, base_path, file_dict):
        for name, content in file_dict.items():
            path = Path(base_path) / name
            if isinstance(content, dict):
                path.mkdir()
                self.create_test_files(path, content)
            else:
                path.write_text(content)
    test_files = {'file1.txt': '', 'file(2).txt': '', 'file[3].png': '', 'file{4}.jpg': '', 'folder1': {'file(5).jpg': '', 'file6.csv': '', 'folder2': {'file[7].csv': '', 'file{8}.png': ''}}}
    temp_dir = ''

    def setUp(self):
        self.temp_dir = os.path.join(os.getcwd(), 'temp_test_dir')
        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)
        self.create_test_files(self.temp_dir, self.test_files)

    def test_case_1(self):
        result = task_func(self.temp_dir)
        self.assertIn(os.path.join(self.temp_dir, 'file(2).txt'), result)
        self.assertIn(os.path.join(self.temp_dir, 'file[3].png'), result)
        self.assertIn(os.path.join(self.temp_dir, 'file{4}.jpg'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'file(5).jpg'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file[7].csv'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file{8}.png'), result)
        self.assertEqual(len(result), 6)

    def test_case_2(self):
        result = task_func(os.path.join(self.temp_dir, 'folder1'))
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'file(5).jpg'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file[7].csv'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file{8}.png'), result)
        self.assertEqual(len(result), 3)

    def test_case_3(self):
        result = task_func(os.path.join(self.temp_dir, 'folder1', 'folder2'))
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file[7].csv'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file{8}.png'), result)
        self.assertEqual(len(result), 2)

    def tearDown(self):
        shutil.rmtree('temp_test_dir')
