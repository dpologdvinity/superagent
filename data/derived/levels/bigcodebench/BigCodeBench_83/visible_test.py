from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
from flask import Flask
from flask_mail import Mail

class TestCases(unittest.TestCase):

    def setUp(self):
        self.smtp_server = 'smtp.example.com'
        self.smtp_port = 587
        self.smtp_user = 'user@example.com'
        self.smtp_password = 'password'
        self.template_folder = 'templates'
        self.app = task_func(self.smtp_server, self.smtp_port, self.smtp_user, self.smtp_password, self.template_folder)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_app_instance(self):
        """Test if the function returns a Flask app instance."""
        self.assertIsInstance(self.app, Flask)

    def test_mail_config(self):
        """Test if the mail configuration is set correctly."""
        self.assertEqual(self.app.config['MAIL_SERVER'], self.smtp_server)
        self.assertEqual(self.app.config['MAIL_PORT'], self.smtp_port)
        self.assertEqual(self.app.config['MAIL_USERNAME'], self.smtp_user)
        self.assertEqual(self.app.config['MAIL_PASSWORD'], self.smtp_password)

    @patch.object(Mail, 'send')
    def test_send_mail_route(self, mock_mail_send):
        """Test if the send_mail route triggers the mail sending."""
        response = self.client.get('/send_mail')
        self.assertEqual(response.status_code, 200)
        mock_mail_send.assert_called_once()
