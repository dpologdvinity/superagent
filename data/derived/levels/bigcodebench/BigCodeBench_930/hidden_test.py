from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random
# Assuming the function is correctly imported from its script
# from task_func import task_func  
class TestCases(unittest.TestCase):
    def test_with_valid_input(self):
        random.seed(0)
        result = task_func('abcdef')
        self.assertEqual(len(result), 3, "Output list should have length 3")
        valid_pairs = ['ab', 'bc', 'cd', 'de', 'ef']
        for pair in result:
            self.assertIn(pair, valid_pairs, f"Pair '{pair}' is not a valid adjacent pair in 'abcdef'")
    def test_single_character(self):
        random.seed(42)
        result = task_func('a')
        expected = ['', '', '']
        self.assertEqual(result, expected, "Should return list of empty strings for a single character")
    def test_empty_string(self):
        random.seed(55)
        result = task_func('')
        expected = ['', '', '']
        self.assertEqual(result, expected, "Should return list of empty strings for an empty string")
    def test_non_letter_input(self):
        random.seed(0)
        with self.assertRaises(ValueError):
            task_func('123')
    def test_long_input(self):
        random.seed(5)
        result = task_func('abcdefghijklmnopqrstuvwxyz')
        all_pairs = [''.join(x) for x in zip('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'[1:])]
        for pair in result:
            self.assertIn(pair, all_pairs, f"Pair '{pair}' is not a valid adjacent pair in the alphabet")
