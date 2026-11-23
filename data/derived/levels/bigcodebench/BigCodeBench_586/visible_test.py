from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from cryptography.fernet import Fernet
import os
import rsa

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_file.txt'
        with open(self.test_file, 'w') as f:
            f.write('This is a test file.')

    def test_file_encryption(self):
        pub_key, encrypted_file, _ = task_func(self.test_file)
        self.assertTrue(os.path.exists(encrypted_file))

    def test_encrypted_key_file_creation(self):
        pub_key, _, encrypted_key_file = task_func(self.test_file)
        self.assertTrue(os.path.exists(encrypted_key_file))

    def test_public_key_type(self):
        pub_key, _, _ = task_func(self.test_file)
        self.assertIsInstance(pub_key, rsa.PublicKey)

    def tearDown(self):
        os.remove(self.test_file)
        encrypted_file = self.test_file + '.encrypted'
        if os.path.exists(encrypted_file):
            os.remove(encrypted_file)
        if os.path.exists('fernet_key.encrypted'):
            os.remove('fernet_key.encrypted')
