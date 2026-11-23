from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup code to create a test log file
        self.test_file_path = "test_log_file.log"
        with open(self.test_file_path, 'w') as f:
            f.write("ERROR 11:30:10 This is an error message\n")
            f.write("WARNING 11:35:10 This is a warning message\n")
    def tearDown(self):
        # Cleanup the test log file
        os.remove(self.test_file_path)
    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func("/path/to/nonexistent/file.log", ['ERROR', 'WARNING'])
    def test_empty_keywords(self):
        self.assertEqual(task_func(self.test_file_path, []), [])
    def test_single_keyword(self):
        result = task_func(self.test_file_path, ['ERROR'])
        self.assertTrue(all('ERROR' in line for line in result))
    def test_multiple_keywords(self):
        result = task_func(self.test_file_path, ['ERROR', 'WARNING'])
        self.assertTrue(all(any(kw in line for kw in ['ERROR', 'WARNING']) for line in result))
    def test_all_keywords(self):
        result = task_func(self.test_file_path, ['ERROR', 'WARNING', 'INFO'])
        self.assertTrue(len(result) >= 2)
