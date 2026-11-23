from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic functionality
        ax = task_func("2021-01-01", "2021-01-10")
        self._common_assertions(ax)
    def test_case_2(self):
        # Test single day range
        ax = task_func("2021-01-01", "2021-01-01")
        self._common_assertions(ax)
    def test_case_3(self):
        # Test leap year
        ax = task_func("2020-02-28", "2020-03-01")
        self._common_assertions(ax)
    def test_case_4(self):
        # Test DST transition
        ax = task_func("2021-03-27", "2021-03-29")
        self._common_assertions(ax)
    def test_case_5(self):
        # Test plotting consistency
        ax = task_func("2021-01-01", "2021-01-10")
        colors = [line.get_color() for line in ax.get_lines()]
        self.assertEqual(len(set(colors)), len(colors))  # Check if colors are unique
    def test_case_6(self):
        # Testing input validation via invalid date format
        with self.assertRaises(ValueError):
            task_func("01-01-2021", "10-01-2021")
    def _common_assertions(self, ax):
        """Common assertions for all test cases"""
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_xlabel(), "Date")
        self.assertEqual(ax.get_ylabel().lower(), "time difference (hours)".lower())
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        expected_timezones = [
            "UTC",
            "America/Los_Angeles",
            "Europe/Paris",
            "Asia/Kolkata",
            "Australia/Sydney",
        ]
        self.assertListEqual(legend_labels, expected_timezones)
    def tearDown(self):
        plt.close("all")
