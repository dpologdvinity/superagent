from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
from bs4 import BeautifulSoup
import unittest
from unittest.mock import patch, MagicMock

class TestCases(unittest.TestCase):
    """Test cases for task_func."""

    @patch('requests.get')
    def test_successful_fetch_and_parse_html_parser(self, mock_get):
        """Test if the function correctly fetches and parses a webpage with valid encoding using html.parser."""
        mock_get.return_value = MagicMock(status_code=200, content=b'Valid HTML content')
        result = task_func('http://example.com', 'utf8')
        self.assertIsInstance(result, BeautifulSoup)

    @patch('requests.get')
    def test_successful_fetch_and_parse_lxml_parser(self, mock_get):
        """Test if the function correctly fetches and parses a webpage with valid encoding using lxml."""
        mock_get.return_value = MagicMock(status_code=200, content=b'Valid HTML content')
        result = task_func('http://example.com', 'utf8', use_lxml=True)
        self.assertIsInstance(result, BeautifulSoup)

    @patch('requests.get')
    def test_connection_error_handling(self, mock_get):
        """Test how the function handles connection errors."""
        mock_get.side_effect = requests.exceptions.ConnectionError()
        result = task_func('http://example.com', 'utf8')
        self.assertIsNone(result)
