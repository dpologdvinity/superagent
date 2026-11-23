from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random

class TestCases(unittest.TestCase):

    def setUp(self):
        random.seed(0)

    def test_return_type(self):
        """ Test that the function returns a list. """
        result = task_func(100, 5)
        self.assertIsInstance(result, list)

    def test_list_length(self):
        """ Test that the length of the list is not greater than the number of unique characters. """
        result = task_func(100, 5)
        self.assertLessEqual(len(result), 26)

    def test_tuple_structure(self):
        """ Test that each element in the list is a tuple with two elements. """
        result = task_func(100, 5)
        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)
