from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random

class TestCases(unittest.TestCase):

    def setUp(self):
        self.vocabulary = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
        random.seed(42)

    def test_case_1(self):
        target_words = ['apple banana', 'banana cherry']
        n_sentences = 1000
        results = task_func(target_words, n_sentences, ['apple', 'banana', 'cherry'])
        self.assertEqual(len(results), n_sentences)
        for target in target_words:
            underscored_target = target.replace(' ', '_')
            self.assertTrue(any((underscored_target in sentence for sentence in results)), f'{underscored_target} not found in any sentences')

    def test_case_2(self):
        target_words = ['apple']
        n_sentences = 1
        results = task_func(target_words, n_sentences, ['apple'] * 10)
        self.assertEqual(len(results), n_sentences)
        self.assertTrue(results[0].count('apple') > 1, "Multiple 'apple' occurrences not replaced correctly")

    def test_case_3(self):
        target_words = []
        n_sentences = 1
        results = task_func(target_words, n_sentences, self.vocabulary)
        self.assertEqual(len(results), n_sentences)
        self.assertTrue(all((' ' in sentence for sentence in results)), '')
