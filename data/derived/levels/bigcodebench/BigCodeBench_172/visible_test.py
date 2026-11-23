from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from datetime import datetime
import json

class TestCases(unittest.TestCase):

    def test_case_1(self):
        utc_datetime = datetime(2024, 4, 15, 12, 0, 0)
        json_data = json.dumps({'utc_datetime': utc_datetime.isoformat()})
        result = task_func(json_data)
        self.assertFalse(result)

    def test_saturday(self):
        utc_datetime = datetime(2024, 4, 13, 12, 0, 0)
        json_data = json.dumps({'utc_datetime': utc_datetime.isoformat()})
        result = task_func(json_data)
        self.assertTrue(result)

    def test_sunday(self):
        utc_datetime = datetime(2024, 4, 14, 12, 0, 0)
        json_data = json.dumps({'utc_datetime': utc_datetime.isoformat()})
        result = task_func(json_data)
        self.assertTrue(result)
