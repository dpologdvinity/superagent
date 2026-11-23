from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    def test_case_1(self):
        text = 'This is a sample text This text contains sample words'
        word_counts = task_func(text).to_dict()
        expected_counts = {'this': 2, 'sample': 2, 'text': 2, 'contains': 1, 'words': 1}
        self.assertDictEqual(word_counts, expected_counts)

    def test_case_2(self):
        text = 'Hello world Hello everyone'
        word_counts = task_func(text).to_dict()
        expected_counts = {'hello': 2, 'world': 1, 'everyone': 1}
        self.assertDictEqual(word_counts, expected_counts)

    def test_case_3(self):
        text = 'a an the in is are'
        word_counts = task_func(text).to_dict()
        expected_counts = {}
        self.assertDictEqual(word_counts, expected_counts)
