from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os

class TestCases(unittest.TestCase):

    def setUp(self):
        """Set up test environment by creating test gzip files with known content."""
        with gzip.open('file1.gz', 'wt') as f:
            f.write('This is a test file.\n')
        with gzip.open('file2.gz', 'wt') as f:
            f.write('This is a different test file.\n')

    def tearDown(self):
        """Clean up by removing the test gzip files."""
        os.remove('file1.gz')
        os.remove('file2.gz')

    def test_identical_files(self):
        """Test that the function returns an empty string for identical files."""
        self.assertEqual(task_func('file1.gz', 'file1.gz'), '')

    def test_different_files(self):
        """Test that the function identifies differences between two files."""
        result = task_func('file1.gz', 'file2.gz')
        self.assertTrue('different' in result)

    def test_first_file_not_exist(self):
        """Test that the function raises FileNotFoundError if the first file does not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent1.gz', 'file2.gz')
