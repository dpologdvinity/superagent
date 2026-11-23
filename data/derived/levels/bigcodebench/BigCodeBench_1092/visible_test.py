from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, Mock

def mock_requests_get(*args, **kwargs):

    class MockResponse:

        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

        def raise_for_status(self):
            if self.status_code != 200:
                raise requests.RequestException('Mocked error')
    if args[0] == 'https://test1.com':
        return MockResponse('<script>{"key": "value"}</script>', 200)
    elif args[0] == 'https://test2.com':
        return MockResponse('<script>{"key1": "value1"}</script><script>{"key2": "value2"}</script>', 200)
    elif args[0] == 'https://test3.com':
        return MockResponse('<div>No script tags here</div>', 200)
    elif args[0] == 'https://test4.com':
        return MockResponse('<script>Not a dictionary</script>', 200)
    elif args[0] == 'https://error.com':
        return MockResponse('Error', 404)
    return MockResponse('', 404)

class TestCases(unittest.TestCase):

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, mock_get):
        result = task_func('https://test1.com')
        self.assertEqual(result, [{'key': 'value'}])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_2(self, mock_get):
        result = task_func('https://test2.com')
        self.assertEqual(result, [{'key1': 'value1'}, {'key2': 'value2'}])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_3(self, mock_get):
        result = task_func('https://test3.com')
        self.assertEqual(result, [])
