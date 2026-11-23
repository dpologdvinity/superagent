from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock, Mock
import os
from python_http_client.exceptions import HTTPError

class TestCases(unittest.TestCase):

    @patch('os.path.exists')
    @patch('sendgrid.SendGridAPIClient.send')
    @patch('os.listdir')
    def test_successful_email_send(self, mock_listdir, mock_send, mock_exists):
        """Test successful email sending with a valid directory."""
        mock_listdir.return_value = ['file1.gz', 'file2.gz']
        mock_exists.return_value = True
        mock_send.return_value = MagicMock(status_code=202)
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        result = task_func('./valid_directory', api_key, recipient_email)
        self.assertTrue(result)

    def test_invalid_directory(self):
        """Test the handling of an invalid directory."""
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        with self.assertRaises(FileNotFoundError):
            task_func('/nonexistent_directory', api_key, recipient_email)

    @patch('os.path.exists')
    @patch('os.listdir')
    @patch('sendgrid.SendGridAPIClient.send')
    def test_failed_email_send(self, mock_send, mock_listdir, mock_exists):
        """Test handling of a failed email send by ensuring HTTPError is raised."""
        mock_listdir.return_value = ['file1.gz', 'file2.gz']
        mock_response = Mock(status_code=400, body='Bad Request')
        mock_exists.return_value = True
        mock_send.side_effect = HTTPError(mock_response, 'Failed to send')
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        with self.assertRaises(HTTPError):
            task_func('./valid_directory', api_key, recipient_email)
