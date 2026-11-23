from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import hashlib
import json
from pathlib import Path
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_empty_directory(self):
        json_file = task_func(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {})

    def test_single_file(self):
        filepath = os.path.join(self.test_dir, 'file1.txt')
        with open(filepath, 'w') as f:
            f.write('Hello, world!')
        json_file = task_func(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertIn(filepath, data.keys())

    def test_multiple_files(self):
        files_content = {'file2.txt': 'Hello again!', 'file3.txt': 'Goodbye!'}
        filepaths = {}
        for filename, content in files_content.items():
            filepath = os.path.join(self.test_dir, filename)
            filepaths[filepath] = content
            with open(filepath, 'w') as f:
                f.write(content)
        json_file = task_func(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            for filepath in filepaths.keys():
                self.assertIn(filepath, data.keys())
