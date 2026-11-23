from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import json
import hashlib
import base64
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup temporary directory for tests
        self.temp_dir = tempfile.mkdtemp()
        # Create sample JSON data for the tests
        self.path_1 = os.path.join(self.temp_dir, 'test1.json')
        self.path_2 = os.path.join(self.temp_dir, 'test2.json')
        sample_data_1 = {
            'A': {
                'B': {
                    'maindata': [{'Info': 'hello world'}],
                },
                'C': {
                    'maindata': [{'Info': 'goodbye world'}],
                }
            }
        }
        sample_data_2 = {
            'A': {
                'D': {
                    'maindata': [{'Info': 'another world'}],
                },
                'E': {
                    'maindata': [{'Info': 'yet another world'}],
                }
            }
        }
        # Write sample data to files
        with open(self.path_1, 'w') as f:
            json.dump(sample_data_1, f)
        with open(self.path_2, 'w') as f:
            json.dump(sample_data_2, f)
    def tearDown(self):
        # Clean up the temporary directory
        os.remove(self.path_1)
        os.remove(self.path_2)
        os.rmdir(self.temp_dir)
    def test_hash_length_for_key_B(self):
        # Check the length of the base64-encoded SHA-256 hash for key B
        result = task_func(self.path_1, 'B')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)
    def test_hash_length_for_key_C(self):
        # Check the length of the base64-encoded SHA-256 hash for key C
        result = task_func(self.path_1, 'C')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)
    def test_hash_length_for_key_D(self):
        # Check the length of the base64-encoded SHA-256 hash for key D
        result = task_func(self.path_2, 'D')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)
    def test_hash_length_for_key_E(self):
        # Check the length of the base64-encoded SHA-256 hash for key E
        result = task_func(self.path_2, 'E')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)
    def test_hash_value_for_key_B(self):
        # Verify the hash value for key B is correctly computed and encoded
        result = task_func(self.path_1, 'B')
        expected_info = 'hello world'
        expected_hash = hashlib.sha256(expected_info.encode()).digest()
        expected_base64 = base64.b64encode(expected_hash).decode()
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(hashed_value, expected_base64)
        os.remove(result)
    def test_hash_value_for_key_C(self):
        # Verify the hash value for key C is correctly computed and encoded
        result = task_func(self.path_1, 'C')
        expected_info = 'goodbye world'
        expected_hash = hashlib.sha256(expected_info.encode()).digest()
        expected_base64 = base64.b64encode(expected_hash).decode()
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(hashed_value, expected_base64)
        os.remove(result)
    def test_invalid_key_error(self):
        # Test handling of invalid key
        with self.assertRaises(KeyError):
            task_func(self.path_1, 'Z')
# Define this function only if needed to run tests manually
