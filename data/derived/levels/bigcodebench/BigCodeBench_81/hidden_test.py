from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
from flask import Flask
class TestCases(unittest.TestCase):
    def setUp(self):
        """Set up test variables."""
        self.api_url = 'https://api.example.com/data'
        self.template_folder = 'templates'
    def test_app_instance(self):
        """Test if the function returns a Flask app instance."""
        app = task_func(self.api_url, self.template_folder)
        self.assertIsInstance(app, Flask)
    def test_api_endpoint_configuration(self):
        """Test if the API endpoint '/data' is configured correctly."""
        app = task_func(self.api_url, self.template_folder)
        with app.test_request_context('/data'):
            self.assertTrue('/data' in [str(route) for route in app.url_map.iter_rules()])
    @patch('requests.get')
    def test_data_endpoint_response(self, mock_get):
        """Test if the data endpoint returns expected JSON data."""
        mock_get.return_value.json.return_value = {'test': 'value'}
        app = task_func(self.api_url, self.template_folder)
        client = app.test_client()
        response = client.get('/data')
        self.assertEqual(response.json, {'test': 'value'})
    @patch('requests.get')
    def test_external_api_call(self, mock_get):
        """Test if the external API is called with the correct URL."""
        mock_get.return_value.status_code = 200  # Assume that the API call is successful
        mock_get.return_value.json.return_value = {'test': 'value'}  # Ensure this returns a serializable dictionary
        app = task_func(self.api_url, self.template_folder)
        client = app.test_client()
        client.get('/data')
        mock_get.assert_called_once_with(self.api_url)
    @patch('requests.get')
    def test_api_endpoint_status_code(self, mock_get):
        """Test if the API endpoint returns the correct status code when accessed."""
        mock_get.return_value.status_code = 200  # Mock the status code as 200
        mock_get.return_value.json.return_value = {'data': 'example'}
        
        app = task_func(self.api_url, self.template_folder)
        client = app.test_client()
        response = client.get('/data')
        self.assertEqual(response.status_code, 200)
