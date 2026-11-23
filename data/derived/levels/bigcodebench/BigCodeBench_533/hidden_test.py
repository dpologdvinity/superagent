from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        # Define the alphabet in the setUp method to be reused in all tests
        self.alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    
    def test_base_conversion_and_hashing(self):
        encoded, salt = task_func('A1', 16, 8, self.alphabet)
        self.assertTrue(isinstance(encoded, str))
        self.assertTrue(isinstance(salt, str))
    def test_different_salts_different_hashes(self):
        result1, salt1 = task_func('FF', 16, 8, self.alphabet)
        result2, salt2 = task_func('FF', 16, 8, self.alphabet)
        self.assertNotEqual(result1, result2)
    def test_invalid_number_format(self):
        with self.assertRaises(ValueError):
            task_func('G', 16, 8, self.alphabet)
    def test_invalid_from_base(self):
        with self.assertRaises(ValueError):
            task_func('10', 1, 8, self.alphabet)
    def test_invalid_to_base(self):
        with self.assertRaises(ValueError):
            task_func('10', 10, 1, self.alphabet)
