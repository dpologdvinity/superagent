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
        text = 'This is the $first $first sentence.'
        plot = task_func(text)
        self.assertIsInstance(plot, plt.Axes, 'Return type should be a plot (Axes).')
        self.is_bar(plot, expected_categories=['$first'], expected_values=[2.0])

    def test_case_2(self):
        text = 'This $is $is $is the $second $sentence $sentence'
        plot = task_func(text)
        self.assertIsInstance(plot, plt.Axes, 'Return type should be a plot (Axes).')
        self.is_bar(plot, expected_categories=['$is', '$second', '$sentence'], expected_values=[3.0, 1.0, 2.0])

    def test_case_3(self):
        text = 'This is the third sentence.'
        plot = task_func(text)
        self.assertIsNone(plot, 'The plot should be None since there are no $ words.')
