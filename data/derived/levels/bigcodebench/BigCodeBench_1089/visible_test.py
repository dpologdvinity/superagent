from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_data = [(5, 'Fruits'), (9, 'Vegetables'), (-1, 'Dairy'), (-2, 'Bakery'), (4, 'Meat')]
        sum_values, count_values = task_func(input_data)
        self.assertEqual(sum_values, 15)
        self.assertEqual(count_values, {'Fruits': 1, 'Vegetables': 1, 'Dairy': 1, 'Bakery': 1, 'Meat': 1})

    def test_case_2(self):
        input_data = [(5, 'Fruits'), (9, 'Fruits'), (-1, 'Fruits'), (-2, 'Fruits')]
        sum_values, count_values = task_func(input_data)
        self.assertEqual(sum_values, 11)
        self.assertEqual(count_values, {'Fruits': 4})

    def test_case_3(self):
        input_data = [(-5, 'Fruits'), (-9, 'Vegetables'), (-1, 'Dairy')]
        sum_values, count_values = task_func(input_data)
        self.assertEqual(sum_values, -15)
        self.assertEqual(count_values, {'Fruits': 1, 'Vegetables': 1, 'Dairy': 1})
