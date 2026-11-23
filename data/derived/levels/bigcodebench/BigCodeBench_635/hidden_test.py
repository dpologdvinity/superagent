from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_simple_text(self):
        """Test with a simple text."""
        text = "hello world"
        matrix, _ = task_func(text)
        self.assertEqual(matrix.shape, (1, 1), "Matrix shape should be (1, 1) for unique words 'hello' and 'world'.")
    def test_text_with_stopwords(self):
        """Test text with stopwords removed."""
        text = "this is a"
        matrix, _ = task_func(text)
        self.assertTrue(matrix.empty, "Matrix should be empty after removing stopwords.")
    def test_duplicate_words(self):
        """Test text with duplicate consecutive words."""
        text = "happy happy joy joy"
        matrix, _ = task_func(text)
        self.assertIn('happy joy', matrix.columns, "Matrix should contain 'happy joy' after duplicates are removed.")
    def test_ngram_range(self):
        """Test with a specific n-gram range."""
        text = "jump high and run fast"
        # Assuming no preprocessing that removes words, we expect 3 unique tri-grams.
        matrix, _ = task_func(text, n=3)
        # Expecting a 3x3 matrix since there are 3 unique tri-grams with no overlap in this simple case.
        self.assertEqual(matrix.shape, (2, 2),
                         "Matrix shape should be (3, 3) for a tri-gram analysis without word removal.")
    def test_empty_text(self):
        """Test with an empty string."""
        text = ""
        matrix, _ = task_func(text)
        self.assertTrue(matrix.empty, "Matrix should be empty for an empty string.")
