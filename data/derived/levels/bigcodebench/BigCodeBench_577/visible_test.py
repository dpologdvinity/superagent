from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import tempfile
import hashlib

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file_path = os.path.join(self.temp_dir.name, 'tést.txt')
        with open(self.test_file_path, 'w') as file:
            file.write('Hello World')

    def test_return_type(self):
        result = task_func(self.temp_dir.name)
        self.assertIsInstance(result, dict)

    def test_file_presence(self):
        result = task_func(self.temp_dir.name)
        self.assertIn('test.txt', result)

    def test_file_size(self):
        result = task_func(self.temp_dir.name)
        self.assertEqual(result['test.txt']['Size'], 11)

    def tearDown(self):
        self.temp_dir.cleanup()
