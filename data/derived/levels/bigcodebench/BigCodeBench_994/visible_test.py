from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import os
import shutil
test_data_1_html = '\n<html>\n    <div class="container">\n        <h1>Title1</h1>\n        <span class="date">Date1</span>\n        <span class="author">Author1</span>\n    </div>\n    <div class="container">\n        <h1>Title2</h1>\n        <span class="date">Date2</span>\n        <span class="author">Author2</span>\n    </div>\n</html>\n'
test_data_2_html = '\n<html>\n    <div class="container">\n        <h1>TitleA</h1>\n        <span class="date">DateA</span>\n        <span class="author">AuthorA</span>\n    </div>\n</html>\n'

class MockResponse:
    """Mock class for requests.Response"""

    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code != 200:
            raise Exception('HTTP Error')

class TestCases(unittest.TestCase):
    """Tests for the task_func function"""

    def setUp(self):
        """Set up any necessary resources before any tests are run."""
        os.makedirs('mnt/data', exist_ok=True)

    @patch('requests.get')
    def test_html_parsing_multiple_entries(self, mock_get):
        """Test parsing of HTML with multiple data entries."""
        mock_get.return_value = MockResponse(test_data_1_html, 200)
        url = 'https://example.com/test_data_1.html'
        csv_file_path = 'mnt/data/output_1.csv'
        expected_output = [('Title1', 'Date1', 'Author1'), ('Title2', 'Date2', 'Author2')]
        self.assertEqual(task_func(url, csv_file_path), expected_output)

    @patch('requests.get')
    def test_html_parsing_single_entry(self, mock_get):
        """Test parsing of HTML with a single data entry."""
        mock_get.return_value = MockResponse(test_data_2_html, 200)
        url = 'https://example.com/test_data_2.html'
        csv_file_path = 'mnt/data/output_2.csv'
        expected_output = [('TitleA', 'DateA', 'AuthorA')]
        self.assertEqual(task_func(url, csv_file_path), expected_output)

    @patch('requests.get')
    def test_html_parsing_with_same_data_as_first(self, mock_get):
        """Test parsing of HTML similar to first test case."""
        mock_get.return_value = MockResponse(test_data_1_html, 200)
        url = 'https://example.com/test_data_1.html'
        csv_file_path = 'mnt/data/output_3.csv'
        expected_output = [('Title1', 'Date1', 'Author1'), ('Title2', 'Date2', 'Author2')]
        self.assertEqual(task_func(url, csv_file_path), expected_output)

    def tearDown(self):
        """Clean up shared resources after all tests in the class have completed."""
        dirs_to_remove = ['mnt/data', 'mnt']
        for dir_path in dirs_to_remove:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)
