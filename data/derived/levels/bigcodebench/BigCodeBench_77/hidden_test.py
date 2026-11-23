from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
from django.http import HttpResponseBadRequest, HttpResponse
from django.conf import settings
if not settings.configured:
    settings.configure()
class TestCases(unittest.TestCase):
    @patch('base64.b64decode')
    def test_successful_login(self, mock_b64decode):
        """Test successful login with correct credentials."""
        mock_b64decode.return_value = b'password'
        data = {'username': 'admin', 'password': 'valid_base64'}
        response = task_func(data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful.', response.content.decode())
    @patch('base64.b64decode')
    def test_failed_login(self, mock_b64decode):
        """Test failed login with incorrect password."""
        mock_b64decode.return_value = b'wrongpassword'
        data = {'username': 'admin', 'password': 'valid_base64'}
        response = task_func(data)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Login failed.', response.content.decode())
    def test_invalid_data_structure(self):
        """Test response with missing username or password."""
        data = {'username': 'admin'}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
    @patch('base64.b64decode', side_effect=ValueError)
    def test_malformed_data(self, mock_b64decode):
        """Test response with non-base64 encoded password."""
        data = {'username': 'admin', 'password': 'not_base64'}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
    def test_empty_data(self):
        """Test response when provided with an empty dictionary."""
        data = {}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
        self.assertIn('Bad Request', response.content.decode())
