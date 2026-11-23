from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pytz
import doctest
from datetime import datetime

class TestCases(unittest.TestCase):

    def test_case_1(self):
        utc_time = datetime(2023, 6, 15, 12, 0, 0, tzinfo=pytz.UTC)
        person_json_str = task_func(utc_time)
        person_data = json.loads(person_json_str)
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        self.assertEqual(person_data['timestamp'], '2023-06-15T12:00:00+00:00')

    def test_case_2(self):
        utc_time = datetime(2022, 5, 10, 10, 30, 0, tzinfo=pytz.UTC)
        person_json_str = task_func(utc_time)
        person_data = json.loads(person_json_str)
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        self.assertEqual(person_data['timestamp'], '2022-05-10T10:30:00+00:00')
        self.assertEqual(person_data['name'], 'David')
        self.assertEqual(person_data['age'], 33)
        self.assertEqual(person_data['city'], 'Mumbai')

    def test_case_3(self):
        utc_time = datetime.utcnow().replace(tzinfo=pytz.UTC)
        person_json_str = task_func(utc_time)
        person_data = json.loads(person_json_str)
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
