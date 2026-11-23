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
        
        # Assert that the returned data has the expected fields and timestamp
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        self.assertEqual(person_data['timestamp'], '2023-06-15T12:00:00+00:00')
        
    def test_case_2(self):
        utc_time = datetime(2022, 5, 10, 10, 30, 0, tzinfo=pytz.UTC)
        person_json_str = task_func(utc_time)
        person_data = json.loads(person_json_str)
        
        # Assert that the returned data has the expected fields and timestamp
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        self.assertEqual(person_data['timestamp'], '2022-05-10T10:30:00+00:00')
        # Test with seed
        self.assertEqual(person_data['name'], 'David')
        self.assertEqual(person_data['age'], 33)
        self.assertEqual(person_data['city'], 'Mumbai')
        
    def test_case_3(self):
        # Test with current UTC time
        utc_time = datetime.utcnow().replace(tzinfo=pytz.UTC)
        person_json_str = task_func(utc_time)
        person_data = json.loads(person_json_str)
        
        # Assert that the returned data has the expected fields and current timestamp
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        
    def test_case_4(self):
        utc_time = datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
        person_json_str = task_func(utc_time, seed=101)
        person_data = json.loads(person_json_str)
        
        # Assert that the returned data has the expected fields and timestamp
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        self.assertEqual(person_data['timestamp'], '2021-01-01T00:00:00+00:00')
        # Test with seed
        self.assertEqual(person_data['name'], 'Grace')
        self.assertEqual(person_data['age'], 29)
        self.assertEqual(person_data['city'], 'Rome')
        
    def test_case_5(self):
        utc_time = datetime(2020, 2, 29, 15, 45, 0, tzinfo=pytz.UTC)  # Leap year date
        person_json_str = task_func(utc_time)
        person_data = json.loads(person_json_str)
        
        # Assert that the returned data has the expected fields and timestamp
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        self.assertEqual(person_data['timestamp'], '2020-02-29T15:45:00+00:00')
