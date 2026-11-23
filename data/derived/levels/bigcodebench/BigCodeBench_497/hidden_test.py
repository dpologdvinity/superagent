from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from datetime import datetime, timedelta
import pytz
import calendar
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1: Default input
        result = task_func()
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for 7 days ago
        expected_date = datetime.now(pytz.UTC) - timedelta(days=7)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_2(self):
        # Input 2: Test with 3 days in the past
        result = task_func(3)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for 3 days ago
        expected_date = datetime.now(pytz.UTC) - timedelta(days=3)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_3(self):
        # Input 3: Test with 0 days in the past (today)
        result = task_func(0)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for today
        expected_date = datetime.now(pytz.UTC)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_4(self):
        # Input 4: Test with 30 days in the past (approximately a month ago)
        result = task_func(30)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for 30 days ago
        expected_date = datetime.now(pytz.UTC) - timedelta(days=30)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_5(self):
        # Input 5: Test handling invalid days_in_the_past
        for invalid in [-1, "1"]:
            with self.assertRaises(Exception):
                task_func(invalid)
