from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch

class TestCases(unittest.TestCase):

    @patch('mechanize.Browser')
    def test_return_type(self, mock_browser):
        """Test that the function returns a list."""
        html_content = "<html><body><a href='https://www.example.com'>Example</a></body></html>"
        mock_browser_instance = mock_browser.return_value
        mock_browser_instance.open.return_value.read.return_value = html_content
        result = task_func('https://www.example.com')
        self.assertIsInstance(result, list)

    @patch('mechanize.Browser')
    def test_extracted_links(self, mock_browser):
        """Test the extracted links from a mock HTML page."""
        html_content = "<html><body><a href='https://www.example.com'>Example</a></body></html>"
        mock_browser_instance = mock_browser.return_value
        mock_browser_instance.open.return_value.read.return_value = html_content
        result = task_func('https://www.example.com')
        self.assertIn('https://www.example.com', result)

    @patch('mechanize.Browser')
    def test_invalid_url(self, mock_browser):
        """Test the function with an invalid URL."""
        mock_browser_instance = mock_browser.return_value
        mock_browser_instance.open.side_effect = mechanize.URLError('Invalid URL')
        with self.assertRaises(mechanize.URLError):
            task_func('invalid_url')
