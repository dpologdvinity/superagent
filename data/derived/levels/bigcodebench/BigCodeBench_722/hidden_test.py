from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, mock_open
class TestCases(unittest.TestCase):
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open, read_data='ERROR\nOK\nERROR')
    @patch('os.remove')
    def test_sample1(self, mock_remove, mock_file, mock_urlretrieve):
        mock_urlretrieve.return_value = ('mock/path/to/file.txt', {'mock': 'headers'})
        result = task_func('http://example.com/log.txt')
        self.assertEqual(result, 2)  # Expecting 2 occurrences of 'ERROR'
    
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open, read_data='OK\nFINE\nGOOD')
    @patch('os.remove')
    def test_sample2(self, mock_remove, mock_file, mock_urlretrieve):
        result = task_func('http://example.com/log.txt')
        self.assertEqual(result, 0)  # Expecting 0 occurrences of 'ERROR'
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.remove')
    def test_sample3(self, mock_remove, mock_file, mock_urlretrieve):
        mock_file.return_value.read.return_value = "ERROR\nERROR\nERROR\nERROR\nERROR"
        mock_urlretrieve.return_value = ('mock/path/to/file.txt', {'mock': 'headers'})
        result = task_func('http://example.com/log.txt')
        self.assertEqual(result, 5)  # Expecting 5 occurrences of 'ERROR'
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.remove')
    def test_mixed_case_errors(self, mock_remove, mock_file, mock_urlretrieve):
        mock_file.return_value.read.return_value = "Error\nerror\nERROR"
        mock_urlretrieve.return_value = ('mock/path/to/file.txt', {'mock': 'headers'})
        result = task_func('http://example.com/log.txt')
        self.assertEqual(result, 1)  # Expecting 1 occurrence of 'ERROR' (case-sensitive)
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.remove')
    def test_large_file(self, mock_remove, mock_file, mock_urlretrieve):
        mock_file.return_value.read.return_value = "ERROR\n" * 5001
        mock_urlretrieve.return_value = ('mock/path/to/file.txt', {'mock': 'headers'})
        result = task_func('http://example.com/log.txt')
        self.assertEqual(result, 5001)  # Expecting 5001 occurrences of 'ERROR'
