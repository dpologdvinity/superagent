from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_time_until_new_year(self):
        # Test with a specific date and timezone
        self.assertIsInstance(task_func('2023-12-31 23:59:59', 'UTC'), int)
    def test_start_of_year(self):
        # Test exactly at the start of a year
        self.assertIsInstance(task_func('2023-01-01 00:00:00', 'UTC'), int)
    def test_leap_year(self):
        # Test a date in a leap year
        self.assertIsInstance(task_func('2024-02-29 00:00:00', 'UTC'), int)
    def test_different_timezone(self):
        # Test with a non-UTC timezone
        self.assertIsInstance(task_func('2023-12-31 23:59:59', 'America/New_York'), int)
    def test_midyear(self):
        # Test a date in the middle of the year
        self.assertIsInstance(task_func('2023-06-15 12:00:00', 'UTC'), int)
