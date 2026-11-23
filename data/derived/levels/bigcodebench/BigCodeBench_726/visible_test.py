from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        random.seed(0)

    def test_extract_english_words(self):
        s = 'This is a test string with some random words: apple, banana, test, hello, world'
        result = task_func(s, 5)
        self.assertTrue(all((word in SAMPLE_ENGLISH_WORDS for word in result)))
        self.assertEqual(len(result), 5)
        self.assertEqual(len(set(result)), len(result), 'All words should be unique')

    def test_fewer_than_n_words(self):
        s = 'hello world'
        result = task_func(s, 5)
        self.assertTrue(len(result) <= 5)
        self.assertTrue(all((word in SAMPLE_ENGLISH_WORDS for word in result)))

    def test_no_english_words(self):
        s = 'xyz abcdef'
        result = task_func(s, 5)
        self.assertEqual(len(result), 0)
