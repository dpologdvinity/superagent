from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock
import smtplib
class TestCases(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_f225(self, mock_smtp):
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Call the function
        result = task_func('{"recipient": "recipient@example.com", "names": ["Josie Smith", "Mugsy Dog Smith"]}')
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert the return value
        self.assertEqual(result, ['Josie Smith', 'Mugsy Dog Smith'])
    @patch('smtplib.SMTP')
    def test_f225_subject(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Call the function
        result = task_func('{"recipient": "names@gmail.com", "names": ["Josie Smith", "Mugsy Dog Smith"]}')
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email@gmail.com', 'your.password')
        mock_smtp_instance.sendmail.assert_called_once_with('your.email@gmail.com', 'names@gmail.com', 'Subject: Extracted Names\n\nJosie Smith\nMugsy Dog Smith')
        
        # Assert the return value
        self.assertEqual(result, ['Josie Smith', 'Mugsy Dog Smith'])
    
    @patch('smtplib.SMTP')
    def test_no_names(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = '{"recipient": "names@gmail.com", "names": []}'
        
        # Call the function with custom input
        result = task_func(input_data=custom_text)
        # Assert the return value
        self.assertEqual(result, [])
    @patch('smtplib.SMTP')
    def test_recepient(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = '{"recipient": "change@gmail.com", "names": []}'
        
        # Call the function with custom input
        result = task_func(input_data=custom_text)
        
        # Assert the return value
        self.assertEqual(result, [])
    @patch('smtplib.SMTP')
    def test_login(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = '{"recipient": "change@gmail.com", "names": ["Name 1", "Name 2"]}'
        
        # Call the function with custom input
        result = task_func(input_data=custom_text, email_address="your.email.change@gmail.com", email_password="your.password.change")
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email.change@gmail.com', 'your.password.change')
        # Assert the return value
        self.assertEqual(result, ["Name 1", "Name 2"])
