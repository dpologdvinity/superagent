from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import tempfile
import hashlib
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory with files for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file_path = os.path.join(self.temp_dir.name, "tést.txt")
        with open(self.test_file_path, "w") as file:
            file.write("Hello World")
    def test_return_type(self):
        result = task_func(self.temp_dir.name)
        self.assertIsInstance(result, dict)
    def test_file_presence(self):
        result = task_func(self.temp_dir.name)
        self.assertIn("test.txt", result)
    def test_file_size(self):
        result = task_func(self.temp_dir.name)
        self.assertEqual(result["test.txt"]["Size"], 11)
    def test_file_hash(self):
        # This test could check the MD5 hash of a known file content
        expected_hash = hashlib.md5("Hello World".encode()).hexdigest()
        result = task_func(self.temp_dir.name)
        normalized_file_name = "test.txt"
        self.assertEqual(result[normalized_file_name]["MD5 Hash"], expected_hash)
    def test_normalized_filename(self):
        # This test could check for filename normalization (ASCII conversion)
        result = task_func(self.temp_dir.name)
        expected_name = "test.txt"
        self.assertIn(expected_name, result)
        self.assertNotIn("tést.txt", result)
    def tearDown(self):
        self.temp_dir.cleanup()
