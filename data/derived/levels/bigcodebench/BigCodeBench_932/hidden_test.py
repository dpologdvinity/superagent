from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_repeating_pairs(self):
        self.assertEqual(task_func("aabbcc"), [('aa', 1)], "Should identify single repeating pair")
        
    def test_mixed_repeating_pairs(self):
        self.assertEqual(task_func("abcabc"), [('ab', 2)], "Should identify most frequent pair in mixed sequence")
        
    def test_single_character(self):
        self.assertEqual(task_func("a"), [], "Should return empty list for single character")
        
    def test_unique_pairs(self):
        self.assertEqual(task_func("abcdef"), [('ab', 1)], "Should handle all unique pairs")
        
    def test_empty_string(self):
        self.assertEqual(task_func(""), [], "Should return empty list for empty string")
    def test_case_insensitive(self):
        # Corrected the expected count to match the correct behavior of the function
        self.assertEqual(task_func("aAaAbbBB"), [('aa', 3)], "Should be case-insensitive")
    def test_ignore_non_alphabetic(self):
        self.assertEqual(task_func("abc123abc!"), [('ab', 2)], "Should ignore non-alphabetic characters")
