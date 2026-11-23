from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def create_file(self, sub_path, content=''):
        full_path = os.path.join(self.test_dir, sub_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as file:
            file.write(content)
        return os.path.normpath(sub_path)

    def test_non_existent(self):
        with self.assertRaises(ValueError):
            task_func(os.path.join(self.test_dir, 'non_existent'))

    def test_empty_folder(self):
        result = task_func(self.test_dir)
        self.assertEqual(result, {})

    def test_files_with_errors(self):
        files = {'1.txt': 'error\nERROR\nErrOr', 'subfolder1/2.txt': '', 'subfolder2/3.txt': 'error\nerror error'}
        expected = {os.path.normpath('1.txt'): 3, os.path.normpath('subfolder1/2.txt'): 0, os.path.normpath('subfolder2/3.txt'): 3}
        for path, content in files.items():
            self.create_file(path, content)
        result = task_func(self.test_dir)
        self.assertEqual(result, expected)
