from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
from functools import reduce

class TestCases(unittest.TestCase):

    def test_case_1(self):
        list_of_pairs = [('Fruits', 5), ('Vegetables', 9), ('Dairy', -1), ('Bakery', -2), ('Meat', 4)]
        expected_output = np.array([360])
        actual_output = task_func(list_of_pairs)
        print(actual_output, expected_output)
        self.assertTrue(np.array_equal(actual_output, expected_output))

    def test_case_2(self):
        list_of_pairs = [('A', 2), ('B', 3), ('C', 4)]
        expected_output = np.array([24])
        actual_output = task_func(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))

    def test_case_3(self):
        list_of_pairs = [('A', -2), ('B', -3), ('C', -4)]
        expected_output = np.array([-24])
        actual_output = task_func(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))
