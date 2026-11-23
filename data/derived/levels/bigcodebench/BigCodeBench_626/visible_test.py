from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from datetime import datetime

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = task_func('2023-06-15 12:00:00', 'UTC')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)

    def test_case_2(self):
        result = task_func('2022-01-01 00:00:00', 'America/New_York')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)

    def test_case_3(self):
        result = task_func('2020-12-31 23:59:59', 'Asia/Shanghai')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)
