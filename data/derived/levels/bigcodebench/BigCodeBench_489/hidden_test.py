from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from datetime import datetime, timedelta
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic functionality - 1 day ago
        epoch_milliseconds = int(
            (datetime.now() - timedelta(days=1)).timestamp() * 1000
        )
        log = task_func(epoch_milliseconds)
        self.assertTrue(isinstance(log, pd.DataFrame))
        self.assertTrue("User" in log.columns)
        self.assertTrue("Activity" in log.columns)
        self.assertTrue("Time" in log.columns)
        start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        self.assertEqual(log.iloc[0]["Time"], start_time)
    def test_case_2(self):
        # Test with a short time frame - 1 minutes ago
        epoch_milliseconds = int(
            (datetime.now() - timedelta(minutes=1)).timestamp() * 1000
        )
        log = task_func(epoch_milliseconds)
        self.assertTrue(len(log) > 0)  # Should have at least one entry
        self.assertTrue(
            log["Time"].min() >= datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        )
    def test_case_3(self):
        # Test with a specific seed
        epoch_milliseconds = int(
            (datetime.now() - timedelta(days=1)).timestamp() * 1000
        )
        seed = 42
        log = task_func(epoch_milliseconds, seed=seed)
        first_row = log.iloc[0]
        expected_user = "user1"
        expected_activity = "login"
        self.assertEqual(first_row["User"], expected_user)
        self.assertEqual(first_row["Activity"], expected_activity)
    def test_case_4(self):
        # Test functionality over a longer period - 1 month ago
        epoch_milliseconds = int(
            (datetime.now() - timedelta(days=30)).timestamp() * 1000
        )
        log = task_func(epoch_milliseconds)
        # Ensure that log timestamps are properly incrementing
        time_diffs = log["Time"].diff().dropna()
        self.assertTrue(all(time_diffs > timedelta(seconds=0)))
        seconds_in_a_month = (
            30 * 24 * 60 * 60
        )  # Approximate number of seconds in a month
        max_possible_entries = (
            seconds_in_a_month  # Assuming a minimum of 1-second increments
        )
        min_possible_entries = (
            seconds_in_a_month // 10
        )  # Assuming a maximum of 10-second increments
        # Verify that the log has a reasonable number of entries given the time frame
        self.assertTrue(min_possible_entries <= len(log) <= max_possible_entries)
        self.assertTrue(
            log["Time"].min() >= datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        )
        self.assertTrue(log["Time"].max() <= datetime.now())
    def test_case_5(self):
        # Test invalid start time (future)
        epoch_milliseconds = int(
            (datetime.now() + timedelta(days=1)).timestamp() * 1000
        )
        with self.assertRaises(Exception):
            task_func(epoch_milliseconds)
