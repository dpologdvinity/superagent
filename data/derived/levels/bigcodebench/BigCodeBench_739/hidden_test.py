from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    
    def test_return_type(self):
        result = task_func()
        self.assertIsInstance(result, float)
    def test_rounded_two_decimal(self):
        result = task_func()
        decimal_part = str(result).split('.')[1]
        self.assertTrue(len(decimal_part) <= 2)
    def test_randomness(self):
        random.seed()  # Reset the seed to ensure randomness
        results = {task_func() for _ in range(100)}
        self.assertTrue(len(results) > 1)
    def test_specific_hex_keys(self):
        for hex_key in KEYS:
            expected_result = round(struct.unpack('!f', bytes.fromhex(hex_key))[0], 2)
            result = task_func(hex_key)
            self.assertEqual(result, expected_result)
    def test_no_seed(self):
        random.seed()  # Reset the random seed
        results = {task_func() for _ in range(100)}
        self.assertTrue(len(results) > 1)
