from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
import tempfile
from unittest.mock import patch

class TestCases(unittest.TestCase):

    def setUp(self):
        self.source_dir = tempfile.mkdtemp()
        self.target_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.target_dir)

    def test_default_directories_and_prefix(self):
        sample_files = ['file1.txt', 'file2.txt', 'file3.txt']
        for file_name in sample_files:
            with open(os.path.join(self.source_dir, file_name), 'w') as f:
                f.write('Sample content for ' + file_name)
        result = task_func(source_dir=self.source_dir, target_dir=self.target_dir)
        expected_files = [os.path.join(self.target_dir, file_name) for file_name in sample_files]
        self.assertListEqual(sorted(result), sorted(expected_files))
        for file in expected_files:
            with open(file, 'r') as f:
                lines = f.readlines()
                self.assertTrue(lines[0].startswith('#Hash: '))
                self.assertIn('Sample content for', ''.join(lines[1:]))

    def test_custom_prefix(self):
        custom_prefix = 'MD5Hash: '
        with open(os.path.join(self.source_dir, 'file.txt'), 'w') as f:
            f.write('Sample content')
        result = task_func(source_dir=self.source_dir, target_dir=self.target_dir, prefix=custom_prefix)
        for file in result:
            with open(file, 'r') as f:
                lines = f.readlines()
                self.assertTrue(lines[0].startswith(custom_prefix))

    def test_empty_directory(self):
        result = task_func(source_dir=self.source_dir, target_dir=self.target_dir)
        self.assertEqual(result, [])
