from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_valid_pattern_matching(self):
        test_length = 100
        test_pattern = '[A-Za-z]{5}'
        test_seed = 12345
        expected_matches = ['mrKBk', 'BqJOl', 'NJlwV', 'UfHVA', 'LGkjn', 'vubDv', 'GSVAa', 'kXLls', 'RKlVy', 'vZcoh', 'FnVZW', 'JQlqL']
        actual_matches = task_func(test_length, test_pattern, seed=test_seed)
        self.assertEqual(actual_matches, expected_matches)

    def test_no_matches_found(self):
        test_length = 100
        test_pattern = 'XYZ'
        test_seed = 12345
        expected_matches = []
        actual_matches = task_func(test_length, test_pattern, seed=test_seed)
        self.assertEqual(actual_matches, expected_matches)

    def test_zero_length_string(self):
        test_length = 0
        test_pattern = '[A-Za-z0-9]{5}'
        expected_matches = []
        actual_matches = task_func(test_length, test_pattern, seed=None)
        self.assertEqual(actual_matches, expected_matches)
