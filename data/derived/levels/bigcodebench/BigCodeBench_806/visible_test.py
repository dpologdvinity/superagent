from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from collections import Counter
import string

class TestCases(unittest.TestCase):

    def test_case_1(self):
        """
        Test Case 1: Simple Text
        - Input: A simple text string with no duplicated words or stopwords
        - Expected Output: A Counter object with the count of each bigram
        """
        text = 'The quick brown fox jumps over the lazy dog.'
        result = task_func(text)
        expected = Counter({('quick', 'brown'): 1, ('brown', 'fox'): 1, ('fox', 'jumps'): 1, ('jumps', 'lazy'): 1, ('lazy', 'dog'): 1})
        self.assertEqual(result, expected)

    def test_case_2(self):
        """
        Test Case 2: Text with Duplicated Words
        - Input: A text string with duplicated consecutive words
        - Expected Output: A Counter object with the count of each bigram, excluding duplicated words
        """
        text = 'This is is a simple simple test test.'
        result = task_func(text)
        expected = Counter({('simple', 'simple'): 1, ('simple', 'test'): 1, ('test', 'test'): 1})
        self.assertEqual(result, expected)

    def test_case_3(self):
        """
        Test Case 3: Text with Stopwords
        - Input: A text string with common English stopwords
        - Expected Output: A Counter object with the count of each bigram, excluding stopwords
        """
        text = 'This is a test of the function.'
        result = task_func(text)
        expected = Counter({('test', 'function'): 1})
        self.assertEqual(result, expected)
