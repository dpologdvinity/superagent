from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_utc_to_est(self):
        """
        Test conversion from UTC to Eastern Standard Time.
        """
        result = task_func("30/03/09 16:31:32.123", "UTC", "America/New_York")
        expected = "30/03/09 12:31:32.123000"  # Adjusted for daylight saving time if applicable
        self.assertEqual(result, expected)
    def test_est_to_utc(self):
        """
        Test conversion from Eastern Standard Time to UTC.
        """
        result = task_func("30/03/09 12:31:32.123", "America/New_York", "UTC")
        expected = "30/03/09 16:31:32.123000"  # Adjusted for daylight saving time if applicable
        self.assertEqual(result, expected)
    def test_utc_to_ist(self):
        """
        Test conversion from UTC to Indian Standard Time.
        """
        result = task_func("01/04/09 00:00:00.000", "UTC", "Asia/Kolkata")
        expected = "01/04/09 05:30:00.000000"  # IST is UTC+5:30
        self.assertEqual(result, expected)
    def test_ist_to_utc(self):
        """
        Test conversion from Indian Standard Time to UTC.
        """
        result = task_func("01/04/09 05:30:00.000", "Asia/Kolkata", "UTC")
        expected = "01/04/09 00:00:00.000000"  # IST is UTC+5:30
        self.assertEqual(result, expected)
    def test_utc_to_gmt(self):
        """
        Test conversion from UTC to GMT (should be the same).
        """
        result = task_func("15/04/09 10:30:00.000", "UTC", "GMT")
        expected = "15/04/09 10:30:00.000000"  # GMT and UTC are the same
        self.assertEqual(result, expected)
