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
        result = task_func()
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        self.assertEqual(result, ['Josie Smith', 'Mugsy Dog Smith'])

    @patch('smtplib.SMTP')
    def test_f225_subject(self, mock_smtp):
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        result = task_func()
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        mock_smtp_instance.login.assert_called_once_with('your.email@gmail.com', 'your.password')
        mock_smtp_instance.sendmail.assert_called_once_with('your.email@gmail.com', 'names@gmail.com', 'Subject: Extracted Names\n\nJosie Smith\nMugsy Dog Smith')
        self.assertEqual(result, ['Josie Smith', 'Mugsy Dog Smith'])

    @patch('smtplib.SMTP')
    def test_no_names(self, mock_smtp):
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        custom_text = '[No names enclosed by square brackets]'
        result = task_func(text=custom_text)
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        mock_smtp_instance.login.assert_called_once_with('your.email@gmail.com', 'your.password')
        mock_smtp_instance.sendmail.assert_called_once_with('your.email@gmail.com', 'names@gmail.com', 'Subject: Extracted Names\n\n')
        self.assertEqual(result, [])
