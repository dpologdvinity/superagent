from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_utc_to_new_york(self):
        """Test conversion from UTC to America/New_York timezone."""
        result = task_func('2022-03-01 12:00:00', 'UTC', 'America/New_York')
        self.assertEqual(result, '2022-03-01 07:00:00')
    def test_utc_to_los_angeles_summer_time(self):
        """Test conversion from UTC to America/Los_Angeles with daylight saving."""
        result = task_func('2022-06-01 12:00:00', 'UTC', 'America/Los_Angeles')
        self.assertEqual(result, '2022-06-01 05:00:00')
    def test_invalid_date_format(self):
        """Test handling of invalid date format."""
        with self.assertRaises(ValueError):
            task_func('invalid-date', 'UTC', 'America/New_York')
    def test_same_timezone_conversion(self):
        """Test conversion where from_tz and to_tz are the same."""
        result = task_func('2022-03-01 12:00:00', 'UTC', 'UTC')
        self.assertEqual(result, '2022-03-01 12:00:00')
    def test_utc_to_london_summer_time(self):
        """Test conversion from UTC to Europe/London during summer (BST)."""
        result = task_func('2022-06-01 12:00:00', 'UTC', 'Europe/London')
        self.assertEqual(result, '2022-06-01 13:00:00')
