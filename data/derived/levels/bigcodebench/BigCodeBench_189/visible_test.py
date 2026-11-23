from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import json
import requests

class TestCases(unittest.TestCase):

    def mock_requests_get(url):
        if url == 'https://api.example.com/data':
            response = requests.Response()
            response._content = json.dumps({'names': ['John', 'Doe', 'Alice']}).encode('utf-8')
            return response
        elif url == 'https://api.example.com/other_data':
            response = requests.Response()
            response._content = json.dumps({'names': ['Bob', '[Adam]', 'Eve']}).encode('utf-8')
            return response
        elif url == 'https://api.example.com/data_1':
            response = requests.Response()
            response._content = json.dumps({'names': ['Billy']}).encode('utf-8')
            return response
        else:
            return ''

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, mock_get):
        context = 'https://api.example.com/data'
        result = task_func(context)
        self.assertListEqual(result, ['John', 'Doe', 'Alice'])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_2(self, mock_get):
        context = 'https://api.example.com/other_data'
        result = task_func(context)
        self.assertListEqual(result, ['Bob', 'Eve'])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_3(self, mock_get):
        context = ''
        result = task_func(context)
        self.assertEqual(result, 'Invalid url input')
