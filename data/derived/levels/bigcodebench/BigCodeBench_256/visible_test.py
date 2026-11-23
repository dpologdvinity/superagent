from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import re
import pytz
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        utc_time = datetime(2023, 6, 15, 12, 0, 0, tzinfo=pytz.UTC)
        password_json_str = task_func(utc_time, seed=79)
        decoded_str = json.loads(password_json_str)
        self.assertEqual(len(decoded_str), 64)
        self.assertTrue(re.match('^[a-f0-9]{64}$', decoded_str))
        self.assertEqual(decoded_str, '3da4b6faf766416fe75b2e5efd831f0fc907e0cc450e7fb58f61110be0a6ab3a')

    def test_case_2(self):
        utc_time = datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
        password_json_str = task_func(utc_time)
        decoded_str = json.loads(password_json_str)
        self.assertEqual(len(decoded_str), 64)
        self.assertTrue(re.match('^[a-f0-9]{64}$', decoded_str))

    def test_case_3(self):
        utc_time = datetime(2050, 12, 31, 23, 59, 59, tzinfo=pytz.UTC)
        password_json_str = task_func(utc_time, salt='random salt be like')
        decoded_str = json.loads(password_json_str)
        self.assertEqual(len(decoded_str), 64)
        self.assertTrue(re.match('^[a-f0-9]{64}$', decoded_str))
        self.assertEqual(decoded_str, 'afd33d74be6cbfb08c6ad76d6f8556ef910e252912d7ebb13603ace3edccd260')
