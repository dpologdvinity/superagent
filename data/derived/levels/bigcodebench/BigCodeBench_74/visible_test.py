from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import unittest.mock as mock
import socket
import requests

class TestCases(unittest.TestCase):

    @mock.patch('socket.gethostbyname')
    @mock.patch('requests.get')
    def test_valid_host(self, mock_get, mock_gethostbyname):
        mock_gethostbyname.return_value = '8.8.8.8'
        mock_get.return_value = mock.Mock(status_code=200, json=lambda: {'city': 'Mountain View', 'country': 'US'})
        result = task_func('google.com')
        self.assertIn('ip_address', result)
        self.assertIn('geolocation', result)
        self.assertEqual(result['ip_address'], '8.8.8.8')
        self.assertEqual(result['geolocation'], {'city': 'Mountain View', 'country': 'US'})

    def test_invalid_host(self):
        with self.assertRaises(ValueError):
            task_func('')

    def test_invalid_host_none(self):
        with self.assertRaises(ValueError):
            task_func(None)
