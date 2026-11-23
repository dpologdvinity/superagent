from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, Mock
import os
def mock_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data
            self.text = json.dumps(json_data)
        
        def json(self):
            return self.json_data
    if args[0] == 'https://api.example.com/data':
        return MockResponse(MOCK_API_RESPONSES.pop(0))
    return MockResponse(None)
MOCK_API_RESPONSES = [
    {"data": ["john.doe@example.com", "jane.smith@domain.org"]},
    {"data": ["123-45-6789", "987-65-4321"]},
    {"data": ["apple", "banana", "cherry"]},
    {"data": []},
    {"data": ["test1@example.com", "test2@domain.org", "123-45-6789", "apple"]}
]
class TestCases(unittest.TestCase):
    def setUp(self):
        if os.path.exists("matched_data.csv"):
            os.remove("matched_data.csv")
    def tearDown(self):
        if os.path.exists("matched_data.csv"):
            os.remove("matched_data.csv")
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, mock_get):
        result = task_func(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
        self.assertTrue(os.path.exists(result))
        with open("matched_data.csv", "r") as file:
            content = file.read()
            self.assertIn("john.doe@example.com", content)
            self.assertIn("jane.smith@domain.org", content)
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_2(self, mock_get):
        result = task_func('\d{3}-\d{2}-\d{4}')
        self.assertTrue(os.path.exists(result))
        with open("matched_data.csv", "r") as file:
            content = file.read()
            self.assertIn("123-45-6789", content)
            self.assertIn("987-65-4321", content)
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_3(self, mock_get):
        result = task_func(r'apple')
        self.assertTrue(os.path.exists(result))
        with open("matched_data.csv", "r") as file:
            content = file.read()
            self.assertIn("apple", content)
            self.assertNotIn("banana", content)
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_4(self, mock_get):
        result = task_func(r'no_match')
        self.assertTrue(os.path.exists(result))
        with open("matched_data.csv", "r") as file:
            content = file.read()
            self.assertEqual(content, "")
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_5(self, mock_get):
        result = task_func(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
        self.assertTrue(os.path.exists(result))
        with open("matched_data.csv", "r") as file:
            content = file.read()
            self.assertNotIn("john.doe@example.com", content)
            self.assertNotIn("jane.smith@domain.org", content)
            self.assertIn("test1@example.com", content)
