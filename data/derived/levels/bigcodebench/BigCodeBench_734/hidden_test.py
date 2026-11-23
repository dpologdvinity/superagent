from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import re
class TestCases(unittest.TestCase):
    def test_case_1(self):
        sentence = "this is an example content"
        # Expected output after removing "content"
        expected_output = {'DT': 2, 'NN': 1, 'VBZ': 1}
        self.assertEqual(task_func(sentence), expected_output)
    def test_case_2(self):
        sentence = "The quick brown fox jumps"
        # "jumps" is removed; expect {'DT': 1, 'JJ': 1, 'NN': 1} for "The quick brown fox"
        expected_output = {'DT': 1, 'JJ': 1, 'NN': 2}
        self.assertEqual(task_func(sentence), expected_output)
    def test_case_3(self):
        sentence = "Over the lazy dog"
        # "dog" is removed; expect {'IN': 1, 'DT': 1, 'JJ': 1} for "Over the lazy"
        expected_output = {'DT': 1, 'IN': 1, 'NN': 1}
        self.assertEqual(task_func(sentence), expected_output)
    def test_case_4(self):
        sentence = "Hello world"
        # "world" is removed; expect {} for "Hello"
        expected_output = {'NN': 1}  # "Hello" might be tagged as interjection 'UH' if not considered a proper noun
        self.assertEqual(task_func(sentence), expected_output)
    def test_case_5(self):
        sentence = "This is a longer sentence with various parts of speech"
        # After removing "speech", adjust expectation
        expected_output = {'DT': 2, 'IN': 2, 'JJ': 1, 'NN': 1, 'NNS': 1, 'RBR': 1, 'VBZ': 1}
        self.assertEqual(task_func(sentence), expected_output)
