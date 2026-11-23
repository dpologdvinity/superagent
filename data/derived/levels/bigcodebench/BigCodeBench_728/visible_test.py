from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, mock_open
import csv

class TestCases(unittest.TestCase):

    def setUp(self):
        self.csv_data = 'Name,Age\nAlice,30\nBob,25\n'

    @patch('os.path.exists', return_value=True)
    @patch('io.open')
    def test_case_1(self, mock_open, mock_exists):
        mock_file_handle = mock_open.return_value.__enter__.return_value
        mock_file_handle.read.return_value = 'Name,Age\nAlice,30\nBob,25\n'
        data, converted_csv = task_func('sample_1.csv', 'utf8', 'utf8', ',')
        expected_data = [{'Name': 'Alice', 'Age': '30'}, {'Name': 'Bob', 'Age': '25'}]
        self.assertEqual(data, expected_data)
        self.assertIn('Alice', converted_csv)
        self.assertIn('Bob', converted_csv)
        mock_open.assert_called_once_with('sample_1.csv', 'r', encoding='utf8')
        mock_file_handle.read.assert_called_once()

    @patch('os.path.exists', return_value=True)
    @patch('io.open')
    def test_different_encoding(self, mock_open, mock_exists):
        mock_open.return_value.__enter__.return_value.read.return_value = self.csv_data.encode('utf-8').decode('cp1251')
        data, converted_csv = task_func('sample_1.csv', 'cp1251', 'utf8', ',')
        self.assertIn('Alice', converted_csv)
        self.assertIn('Bob', converted_csv)

    @patch('io.open', new_callable=mock_open, read_data='Name,Age\nAlice,30\nBob,25\n')
    def test_empty_file(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = ''
        data, converted_csv = task_func('empty.csv', 'utf8', 'utf8', ',')
        self.assertEqual(data, [])
        self.assertEqual(converted_csv.strip(), 'Column')
