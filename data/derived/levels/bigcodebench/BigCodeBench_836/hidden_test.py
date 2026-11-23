from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import tempfile
import shutil
import os
from unittest.mock import mock_open, patch, MagicMock
import csv
class TestCases(unittest.TestCase):
    def setUp(self):
        # Common setup for all tests
        self.target_value = '332'
        self.csv_dir = '/fake/csv_files/'
        self.processed_dir = '/fake/processed_files/'
        self.simulate = True
    @patch('os.listdir', return_value=['file_with_target.csv'])
    @patch('builtins.open', new_callable=mock_open, read_data="332,Data\n333,More Data\n")
    @patch('shutil.move')
    def test_file_with_target(self, mock_move, mock_open, mock_listdir):
        """ Test case for files with the target value. """
        result = task_func(target_value=self.target_value, csv_dir=self.csv_dir,
                       processed_dir=self.processed_dir, simulate=self.simulate)
        self.assertIn('file_with_target.csv', result)
        self.assertEqual(result['file_with_target.csv'], 0)
        mock_move.assert_not_called()
    @patch('os.listdir', return_value=['file_without_target.csv'])
    @patch('builtins.open', new_callable=mock_open, read_data="334,Data\n335,More Data\n")
    @patch('shutil.move')
    def test_file_without_target(self, mock_move, mock_open, mock_listdir):
        """ Test case for files without the target value. """
        result = task_func(target_value=self.target_value, csv_dir=self.csv_dir,
                       processed_dir=self.processed_dir, simulate=self.simulate)
        self.assertNotIn('file_without_target.csv', result)
        mock_move.assert_not_called()
    @patch('os.listdir', return_value=['empty_file.csv'])
    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('shutil.move')
    def test_empty_file(self, mock_move, mock_open, mock_listdir):
        """ Test case for an empty CSV file. """
        result = task_func(target_value=self.target_value, csv_dir=self.csv_dir,
                       processed_dir=self.processed_dir, simulate=self.simulate)
        self.assertNotIn('empty_file.csv', result)
        mock_move.assert_not_called()
    @patch('os.listdir', return_value=['file_with_multiple_targets.csv'])
    @patch('builtins.open', new_callable=mock_open, read_data="332,Data\n332,More Data\n333,Other Data\n")
    @patch('shutil.move')
    def test_file_with_multiple_targets(self, mock_move, mock_open, mock_listdir):
        """ Test case for files with multiple occurrences of the target value. """
        result = task_func(target_value=self.target_value, csv_dir=self.csv_dir,
                       processed_dir=self.processed_dir, simulate=self.simulate)
        self.assertIn('file_with_multiple_targets.csv', result)
        self.assertEqual(result['file_with_multiple_targets.csv'], 0)
        mock_move.assert_not_called()
    @patch('os.listdir', return_value=['file_with_target_not_first.csv'])
    @patch('builtins.open', new_callable=mock_open, read_data="333,Data\n334,332\n335,Data\n")
    @patch('shutil.move')
    def test_file_with_target_not_first(self, mock_move, mock_open, mock_listdir):
        """ Test case for a file where the target value is not in the first cell. """
        result = task_func(target_value='332', csv_dir=self.csv_dir,
                    processed_dir=self.processed_dir, simulate=self.simulate)
        # This file should not be in the results because '332' is not in the first cell
        self.assertNotIn('file_with_target_not_first.csv', result)
        mock_move.assert_not_called()
