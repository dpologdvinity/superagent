from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, ANY
import os
import csv
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.addCleanup(lambda: os.rmdir(self.test_dir))

    def tearDown(self):
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))

    @patch('requests.get')
    def test_extraction_and_saving_default(self, mock_get):
        """Test extracting emails using default parameters and saving to default path."""
        mocked_html_content = '<html><body>Emails: test1@example.com, test2@domain.com</body></html>'
        mock_get.return_value.text = mocked_html_content
        csv_path = os.path.join(self.test_dir, 'emails.csv')
        with patch('builtins.open', unittest.mock.mock_open()) as mocked_file:
            task_func(csv_path=csv_path)
            args, kwargs = mocked_file.call_args
            self.assertEqual(args[0], csv_path)
            try:
                self.assertEqual(kwargs['mode'], 'w')
            except:
                self.assertEqual(args[1], 'w')
            self.assertEqual(kwargs['newline'], '')

    @patch('requests.get')
    def test_extraction_custom_url(self, mock_get):
        """Test the email extraction from a custom URL and ensure file creation even if no emails are found."""
        mock_get.return_value.text = '<html><body>No email here</body></html>'
        csv_path = os.path.join(self.test_dir, 'output.csv')
        result = task_func(url='http://mocked-url.com', csv_path=csv_path)
        self.assertEqual(result, csv_path)
        self.assertTrue(os.path.exists(csv_path))
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        self.assertEqual(data, [['Emails']])

    @patch('requests.get')
    def test_extraction_custom_regex(self, mock_get):
        """Test extraction with a custom regex pattern."""
        mocked_html_content = '<html><body>Email: unique@example.com, other@sample.com</body></html>'
        mock_get.return_value.text = mocked_html_content
        csv_path = os.path.join(self.test_dir, 'custom_regex.csv')
        task_func(csv_path=csv_path, regex='\\b[A-Za-z0-9._%+-]+@example.com\\b')
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            emails = [row for row in reader]
        self.assertEqual(emails, [['Emails'], ['unique@example.com']])
