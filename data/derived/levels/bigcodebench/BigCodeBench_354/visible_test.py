from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        sentences_dict = {'Sentence1': 'the quick brown fox', 'Sentence2': 'jumps over the lazy dog', 'Sentence3': 'the dog is brown'}
        word_keys = ['the', 'dog']
        ax = task_func(sentences_dict, word_keys)
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 2, 3, 2])

    def test_case_2(self):
        sentences_dict = {'Sentence1': 'apple orange banana', 'Sentence2': 'apple apple', 'Sentence3': 'banana orange orange'}
        word_keys = ['apple', 'orange', 'banana']
        ax = task_func(sentences_dict, word_keys)
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 3, 2, 3, 3, 2])

    def test_case_3(self):
        sentences_dict = {'Sentence1': 'cat mouse', 'Sentence2': 'dog cat', 'Sentence3': 'mouse mouse cat'}
        word_keys = ['cat', 'mouse', 'dog']
        ax = task_func(sentences_dict, word_keys)
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 3, 1, 3, 3, 1])
