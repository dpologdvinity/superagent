from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from faker import Faker
import itertools
import statistics
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        elements = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        subset_size = 2
        result = task_func(elements, subset_size)
        self.assertEqual(result, {'mean': 11, 'median': 11, 'mode': 11})

    def test_case_2(self):
        elements = (1, 2, 2, 3, 4)
        subset_size = 2
        result = task_func(elements, subset_size)
        self.assertEqual(result, {'mean': 4.8, 'median': 5.0, 'mode': 5})

    def test_case_3(self):
        elements = (1, 2, 3, 4, 5)
        subset_size = 4
        result = task_func(elements, subset_size)
        self.assertEqual(result, {'mean': 12, 'median': 12, 'mode': 10})
