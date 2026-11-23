from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Regular list of tuples with different categories
        input_data = [(5, 'Fruits'), (9, 'Vegetables'), (-1, 'Dairy'), (-2, 'Bakery'), (4, 'Meat')]
        sum_values, count_values = task_func(input_data)
        self.assertEqual(sum_values, 15)
        self.assertEqual(count_values, {'Fruits': 1, 'Vegetables': 1, 'Dairy': 1, 'Bakery': 1, 'Meat': 1})
    def test_case_2(self):
        # List of tuples with all the same categories
        input_data = [(5, 'Fruits'), (9, 'Fruits'), (-1, 'Fruits'), (-2, 'Fruits')]
        sum_values, count_values = task_func(input_data)
        self.assertEqual(sum_values, 11)
        self.assertEqual(count_values, {'Fruits': 4})
    def test_case_3(self):
        # List of tuples with all negative numeric values
        input_data = [(-5, 'Fruits'), (-9, 'Vegetables'), (-1, 'Dairy')]
        sum_values, count_values = task_func(input_data)
        self.assertEqual(sum_values, -15)
        self.assertEqual(count_values, {'Fruits': 1, 'Vegetables': 1, 'Dairy': 1})
    def test_case_4(self):
        # Empty list
        input_data = []
        sum_values, count_values = task_func(input_data)
        self.assertEqual(sum_values, 0)
        self.assertEqual(count_values, {})
    def test_case_5(self):
        # List of tuples with mixed positive and negative numeric values for the same category
        input_data = [(5, 'Fruits'), (-5, 'Fruits'), (3, 'Fruits')]
        sum_values, count_values = task_func(input_data)
        self.assertEqual(sum_values, 3)
        self.assertEqual(count_values, {'Fruits': 3})
    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(task_func([]), (0, {}))
    def test_all_negative_values(self):
        """Test with all negative numeric values."""
        list_of_tuples = [(-5, 'Fruits'), (-2, 'Vegetables')]
        self.assertEqual(task_func(list_of_tuples), (-7, {'Fruits': 1, 'Vegetables': 1}))
    def test_duplicate_categories(self):
        """Test with duplicate categories."""
        list_of_tuples = [(1, 'Fruits'), (2, 'Fruits'), (3, 'Vegetables')]
        self.assertEqual(task_func(list_of_tuples), (6, {'Fruits': 2, 'Vegetables': 1}))
    def test_single_tuple_in_list(self):
        """Test with a single tuple in the list."""
        list_of_tuples = [(10, 'Meat')]
        self.assertEqual(task_func(list_of_tuples), (10, {'Meat': 1}))
    def test_float_numeric_values(self):
        """Test with non-integer numeric values (floats)."""
        list_of_tuples = [(1.5, 'Fruits'), (2.5, 'Vegetables')]
        self.assertEqual(task_func(list_of_tuples), (4.0, {'Fruits': 1, 'Vegetables': 1}))
