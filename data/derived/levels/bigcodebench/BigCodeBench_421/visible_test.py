from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, Mock
import os
TEST_URL = 'https://www.example.com'
TEST_DIRECTORY = './test_uploads_task_func'
TEST_DIRECTORY_EMPTY = './test_uploads_task_func_empty'
TEST_METADATA = {'userId': 'abc'}

def mock_requests_post(*args, **kwargs):

    class MockResponse:

        def __init__(self, status_code):
            self.status_code = status_code
    return MockResponse(200)

def mock_requests_post_fail(*args, **kwargs):

    class MockResponse:

        def __init__(self, status_code):
            self.status_code = status_code
    return MockResponse(400)

class TestCases(unittest.TestCase):

    def setUp(self):
        os.makedirs(TEST_DIRECTORY, exist_ok=True)
        for i in range(5):
            with open(os.path.join(TEST_DIRECTORY, f'test_file_{i}.txt'), 'w') as f:
                f.write(f'This is test file {i}')
        os.makedirs(TEST_DIRECTORY_EMPTY, exist_ok=True)

    def tearDown(self):
        if os.path.exists(TEST_DIRECTORY):
            for file in os.listdir(TEST_DIRECTORY):
                os.remove(os.path.join(TEST_DIRECTORY, file))
            os.rmdir(TEST_DIRECTORY)
        if os.path.exists(TEST_DIRECTORY_EMPTY):
            os.rmdir(TEST_DIRECTORY_EMPTY)

    @patch('requests.post', side_effect=mock_requests_post)
    def test_upload_success(self, mock_post):
        status_codes = task_func(TEST_URL, TEST_DIRECTORY, TEST_METADATA)
        self.assertEqual(status_codes, [200, 200, 200, 200, 200])

    @patch('requests.post', side_effect=mock_requests_post)
    def test_directory_not_found(self, mock_post):
        with self.assertRaises(FileNotFoundError):
            task_func(TEST_URL, 'non_existing_directory', TEST_METADATA)

    @patch('requests.post', side_effect=mock_requests_post)
    def test_empty_directory(self, mock_post):
        status_codes = task_func(TEST_URL, TEST_DIRECTORY_EMPTY, TEST_METADATA)
        self.assertEqual(status_codes, [])
