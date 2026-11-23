from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import blake3
import hashlib

class TestCases(unittest.TestCase):

    def setUp(self):
        """Set up common test data."""
        self.req_data = {'key': 'value'}
        self.empty_data = {}
        self.diff_data1 = {'data': 'test1'}
        self.diff_data2 = {'data': 'test2'}

    def compute_hex_md5(self):
        """Helper to compute the blake3 hex and md5"""
        json_req_data = json.dumps(self.diff_data1)
        blake3_hex = blake3.blake3(json_req_data.encode('utf-8')).hexdigest()
        md5_hash = hashlib.md5(blake3_hex.encode('utf-8')).hexdigest()
        return (blake3_hex, md5_hash)

    def test_return_types(self):
        """Ensure the function returns a tuple of strings."""
        blake3_hash, md5_hash = task_func(self.req_data)
        self.assertIsInstance(blake3_hash, str)
        self.assertIsInstance(md5_hash, str)

    def test_blake3_length(self):
        """Test the length of the BLAKE3 hash."""
        blake3_hash, _ = task_func(self.req_data)
        self.assertEqual(len(blake3_hash), 64)

    def test_md5_length(self):
        """Test the length of the MD5 hash."""
        _, md5_hash = task_func(self.req_data)
        self.assertEqual(len(md5_hash), 32)
