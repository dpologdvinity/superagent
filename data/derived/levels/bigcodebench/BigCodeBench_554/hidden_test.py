from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
# Constants for testing
MIN_WORDS = 3
MAX_WORDS = 10
WORDS_POOL = ['apple', 'banana', 'racecar', 'world', 'level', 'madam', 'radar', 'rotor']
class TestCases(unittest.TestCase):
    def test_is_palindrome(self):
        """Test that the sentence generated is a palindrome."""
        sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
        processed_sentence = " ".join(sentence.split()[::-1])
        self.assertEqual(processed_sentence, sentence)
    def test_sentence_length_within_range(self):
        """Test that the sentence length is within the specified range."""
        sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
        length = len(sentence.split())
        self.assertTrue(MIN_WORDS <= length <= MAX_WORDS)
    def test_multiple_sentences(self):
        """Test that multiple generated sentences are palindromes."""
        for _ in range(5):
            sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
            processed_sentence = " ".join(sentence.split()[::-1])
            self.assertEqual(processed_sentence, sentence)
    def test_word_choice_from_pool(self):
        """Test that all words in the sentence are from the provided word pool."""
        sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
        words = sentence.split()
        for word in words:
            self.assertIn(word, WORDS_POOL)
    def test_symmetry_of_sentence(self):
        """Test that the sentence is symmetric around its center."""
        sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
        words = sentence.split()
        mid = len(words) // 2
        if len(words) % 2 == 0:
            self.assertEqual(words[:mid], words[:-mid-1:-1])
        else:
            self.assertEqual(words[:mid], words[-mid:][::-1])
