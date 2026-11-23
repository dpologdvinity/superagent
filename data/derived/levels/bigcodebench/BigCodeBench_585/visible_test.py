from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import rsa
import os
import zipfile
from base64 import b64encode
import unittest
import tempfile
import shutil

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        if os.path.exists('encrypted_files.zip'):
            os.remove('encrypted_files.zip')

    def test_return_type(self):
        for i in range(2):
            with open(os.path.join(self.test_dir, f'file{i}.txt'), 'w') as f:
                f.write('Sample content')
        pub_key, zipfile_name = task_func(self.test_dir)
        self.assertIsInstance(pub_key, rsa.PublicKey)
        self.assertIsInstance(zipfile_name, str)

    def test_zipfile_creation(self):
        for i in range(2):
            with open(os.path.join(self.test_dir, f'file{i}.txt'), 'w') as f:
                f.write('Sample content')
        _, zipfile_name = task_func(self.test_dir)
        self.assertTrue(os.path.exists(zipfile_name))
        with zipfile.ZipFile(zipfile_name, 'r') as zipf:
            self.assertEqual(len(zipf.namelist()), 2)

    def test_empty_directory(self):
        _, zipfile_name = task_func(self.test_dir)
        with zipfile.ZipFile(zipfile_name, 'r') as zipf:
            self.assertEqual(len(zipf.namelist()), 0)
