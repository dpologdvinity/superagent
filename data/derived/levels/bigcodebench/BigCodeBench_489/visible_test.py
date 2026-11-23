from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from datetime import datetime, timedelta

class TestCases(unittest.TestCase):

    def test_case_1(self):
        epoch_milliseconds = int((datetime.now() - timedelta(days=1)).timestamp() * 1000)
        log = task_func(epoch_milliseconds)
        self.assertTrue(isinstance(log, pd.DataFrame))
        self.assertTrue('User' in log.columns)
        self.assertTrue('Activity' in log.columns)
        self.assertTrue('Time' in log.columns)
        start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        self.assertEqual(log.iloc[0]['Time'], start_time)

    def test_case_2(self):
        epoch_milliseconds = int((datetime.now() - timedelta(minutes=1)).timestamp() * 1000)
        log = task_func(epoch_milliseconds)
        self.assertTrue(len(log) > 0)
        self.assertTrue(log['Time'].min() >= datetime.fromtimestamp(epoch_milliseconds / 1000.0))

    def test_case_3(self):
        epoch_milliseconds = int((datetime.now() - timedelta(days=1)).timestamp() * 1000)
        seed = 42
        log = task_func(epoch_milliseconds, seed=seed)
        first_row = log.iloc[0]
        expected_user = 'user1'
        expected_activity = 'login'
        self.assertEqual(first_row['User'], expected_user)
        self.assertEqual(first_row['Activity'], expected_activity)
