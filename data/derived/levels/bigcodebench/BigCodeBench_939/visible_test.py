from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from pathlib import Path
import shutil

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = Path('temp_test_dir')
        self.temp_dir.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_special_characters_removal(self):
        test_files = ['file@1.txt', 'file_#2.txt', 'file$ 3.txt']
        for file_name in test_files:
            (self.temp_dir / file_name).touch()
        expected_names = ['file1txt', 'file2txt', 'file3txt']
        new_file_names = task_func(str(self.temp_dir))
        self.assertListEqual(sorted(new_file_names), sorted(expected_names))

    def test_alphanumeric_names(self):
        test_files = ['file1.txt', 'file2.txt', 'file3.txt']
        for file_name in test_files:
            (self.temp_dir / file_name).touch()
        expected_names = ['file1txt', 'file2txt', 'file3txt']
        new_file_names = task_func(str(self.temp_dir))
        self.assertListEqual(sorted(new_file_names), sorted(expected_names))

    def test_empty_directory(self):
        expected_names = []
        new_file_names = task_func(str(self.temp_dir))
        self.assertListEqual(new_file_names, expected_names)
