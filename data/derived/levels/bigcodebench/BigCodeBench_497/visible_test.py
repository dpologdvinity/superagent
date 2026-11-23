from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from datetime import datetime, timedelta
import pytz
import calendar

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = task_func()
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        expected_date = datetime.now(pytz.UTC) - timedelta(days=7)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)

    def test_case_2(self):
        result = task_func(3)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        expected_date = datetime.now(pytz.UTC) - timedelta(days=3)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)

    def test_case_3(self):
        result = task_func(0)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        expected_date = datetime.now(pytz.UTC)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
