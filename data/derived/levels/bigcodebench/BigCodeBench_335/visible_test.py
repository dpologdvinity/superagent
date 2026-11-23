from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import collections

class TestCases(unittest.TestCase):

    def test_default_length(self):
        random.seed(0)
        freq = task_func()
        self.assertIsInstance(freq, collections.OrderedDict, 'Output should be an OrderedDict')
        self.assertEqual(sum(freq.values()), 100, 'Total count of letters should be 100 for default length')
        self.assertTrue(all((freq[key] >= freq[key2] for key, key2 in zip(list(freq)[:-1], list(freq)[1:]))), 'Frequencies should be sorted in descending order')

    def test_specific_length(self):
        random.seed(0)
        freq = task_func(50)
        self.assertIsInstance(freq, collections.OrderedDict, 'Output should be an OrderedDict')
        self.assertEqual(sum(freq.values()), 50, 'Total count of letters should be 50 for specific length')
        self.assertTrue(all((freq[key] >= freq[key2] for key, key2 in zip(list(freq)[:-1], list(freq)[1:]))), 'Frequencies should be sorted in descending order')

    def test_minimum_length(self):
        random.seed(0)
        freq = task_func(1)
        self.assertIsInstance(freq, collections.OrderedDict, 'Output should be an OrderedDict')
        self.assertEqual(sum(freq.values()), 1, 'Total count of letters should be 1 for minimum length')
        self.assertEqual(len(freq), 1, 'Only one letter should be present for minimum length')
