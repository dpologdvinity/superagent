from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    @staticmethod
    def is_barplot(ax, expected_values, expected_categories):
        extracted_values = [bar.get_height() for bar in ax.patches]
        extracted_categories = [tick.get_text() for tick in ax.get_xticklabels()]
        for actual_value, expected_value in zip(extracted_values, expected_values):
            assert actual_value == expected_value, f"Expected value '{expected_value}', but got '{actual_value}'"
        for actual_category, expected_category in zip(extracted_categories, expected_categories):
            assert actual_category == expected_category, f"Expected category '{expected_category}', but got '{actual_category}'"

    def test_case_1(self):
        car_dict = {'Ford': 'Red', 'Toyota': 'Blue', 'Mercedes': 'Black', 'Tesla': 'White', 'BMW': 'Silver'}
        df, ax = task_func(car_dict)
        self.is_barplot(ax, expected_values=[1, 1, 1, 1, 1], expected_categories=['Red', 'Blue', 'Black', 'White', 'Silver'])
        self.assertListEqual(list(df.columns), ['Car', 'Color'])
        self.assertSetEqual(set(df['Car']), set(car_dict.keys()))
        self.assertSetEqual(set(df['Color']), set(car_dict.values()))
        self.assertEqual(ax.get_title(), 'Distribution of Vehicle Colors')
        self.assertEqual(ax.get_xlabel(), 'Color')
        self.assertEqual(ax.get_ylabel(), 'Frequency')

    def test_case_2(self):
        car_dict = {'Ford': 'Blue', 'Toyota': 'Red', 'Fiat': 'Silver', 'Tesla': 'Silver', 'BMW': 'White'}
        df, ax = task_func(car_dict)
        self.assertListEqual(list(df.columns), ['Car', 'Color'])
        self.assertSetEqual(set(df['Car']), set(car_dict.keys()))
        self.assertSetEqual(set(df['Color']), set(car_dict.values()))
        self.assertEqual(ax.get_title(), 'Distribution of Vehicle Colors')

    def test_case_3(self):
        car_dict = {'Ford': 'Red', 'Toyota': 'Blue', 'Mercedes': 'Black', 'Tesla': 'White', 'BMW': 'Silver', 'Lamborghini': 'Black', 'Peugeot': 'Black'}
        df, ax = task_func(car_dict)
        self.assertListEqual(list(df.columns), ['Car', 'Color'])
        self.assertSetEqual(set(df['Car']), set(car_dict.keys()))
        self.assertSetEqual(set(df['Color']), set(car_dict.values()))
        self.assertEqual(ax.get_title(), 'Distribution of Vehicle Colors')
