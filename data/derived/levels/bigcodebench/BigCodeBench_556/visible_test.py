from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        self.s = 'example'
        self.min_length = 5
        self.max_length = 10
        self.letters = 'abcdefghijklmnopqrstuvwxyz'

    def test_length_of_generated_string(self):
        generated_s, _ = task_func(self.s, self.min_length, self.max_length, self.letters)
        self.assertTrue(self.min_length <= len(generated_s) <= self.max_length)

    def test_similarity_boolean(self):
        _, is_similar = task_func(self.s, self.min_length, self.max_length, self.letters)
        self.assertIsInstance(is_similar, bool)

    def test_empty_string(self):
        s = ''
        generated_s, is_similar = task_func(s, self.min_length, self.max_length, self.letters)
        self.assertTrue(isinstance(generated_s, str))
        self.assertTrue(isinstance(is_similar, bool))
