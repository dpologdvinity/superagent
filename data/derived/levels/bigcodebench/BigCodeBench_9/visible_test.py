from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    @staticmethod
    def is_bar(ax, expected_values, expected_categories):
        extracted_values = [bar.get_height() for bar in ax.patches]
        extracted_categories = [tick.get_text() for tick in ax.get_xticklabels()]
        for actual_value, expected_value in zip(extracted_values, expected_values):
            assert actual_value == expected_value, f"Expected value '{expected_value}', but got '{actual_value}'"
        for actual_category, expected_category in zip(extracted_categories, expected_categories):
            assert actual_category == expected_category, f"Expected category '{expected_category}', but got '{actual_category}'"

    def test_case_1(self):
        df, ax = task_func([('Allison', 49), ('Cassidy', 72), ('Jamie', -74), ('Randy', -25), ('Joshua', -85)])
        self.assertEqual(df['Category'].tolist(), ['Allison', 'Cassidy', 'Jamie', 'Randy', 'Joshua'])
        self.assertEqual(df['Value'].tolist(), [49, 72, -74, -25, -85])
        self.assertEqual(ax.get_title(), 'Category vs Value')
        self.is_bar(ax=ax, expected_categories=['Allison', 'Cassidy', 'Jamie', 'Randy', 'Joshua'], expected_values=[49, 72, -74, -25, -85])

    def test_case_2(self):
        df, ax = task_func([('Jonathan', 36), ('Maureen', 47), ('Zachary', -32), ('Kristen', 39), ('Donna', -23)])
        self.assertEqual(df['Category'].tolist(), ['Jonathan', 'Maureen', 'Zachary', 'Kristen', 'Donna'])
        self.assertEqual(df['Value'].tolist(), [36, 47, -32, 39, -23])
        self.assertEqual(ax.get_title(), 'Category vs Value')

    def test_case_3(self):
        df, ax = task_func([('Eric', -91), ('Jennifer', 52), ('James', -79), ('Matthew', 25), ('Veronica', 2)])
        self.assertEqual(df['Category'].tolist(), ['Eric', 'Jennifer', 'James', 'Matthew', 'Veronica'])
        self.assertEqual(df['Value'].tolist(), [-91, 52, -79, 25, 2])
        self.assertEqual(ax.get_title(), 'Category vs Value')
