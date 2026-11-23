from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import rsa
import base64
from unittest.mock import patch

class TestCases(unittest.TestCase):

    def setUp(self):
        """Set up test environment: create necessary files with mock content."""
        with open('example.txt', 'w') as f:
            f.write('This is a test file.')
        with open('empty.txt', 'w') as f:
            f.write('')
        pub_key, priv_key = rsa.newkeys(512)
        with open('private.pem', 'wb') as f:
            f.write(priv_key.save_pkcs1('PEM'))
        with open('invalid_private.pem', 'w') as f:
            f.write('Invalid key content')

    def tearDown(self):
        """Clean up by removing the files created for the test."""
        for filename in ['example.txt', 'empty.txt', 'private.pem', 'invalid_private.pem']:
            if os.path.exists(filename):
                os.remove(filename)

    def test_signed_hash_of_file(self):
        """Ensure a non-empty signature is produced for a file with content."""
        result = task_func('example.txt')
        self.assertTrue(len(result) > 0)

    def test_signed_hash_of_empty_file(self):
        """Ensure a non-empty signature is produced for an empty file."""
        result = task_func('empty.txt')
        self.assertTrue(len(result) > 0)

    def test_file_not_exist(self):
        """Verify FileNotFoundError is raised for non-existent file paths."""
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent.txt')
