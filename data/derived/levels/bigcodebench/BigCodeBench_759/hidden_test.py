from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock, call
import shutil
import os
import fnmatch
class TestCases(unittest.TestCase):
    def setUp(self):
        self.source_directory = "/fake/source_directory"
        self.destination_directory = "/fake/destination_directory"
        self.files = ['file1.txt', 'file2.txt', 'image.jpg', 'data.log', 'report.TXT', 'config file.cfg']
    @patch('os.walk')
    @patch('shutil.move')
    def test_no_files_to_move(self, mock_move, mock_walk):
        mock_walk.return_value = [(self.source_directory, [], ['image.jpg', 'data.log', 'config file.cfg'])]
        result = task_func(self.source_directory, self.destination_directory, '*.txt')
        self.assertEqual(result, [])
        mock_move.assert_not_called()
    @patch('os.walk')
    @patch('shutil.move')
    def test_non_existing_source_directory(self, mock_move, mock_walk):
        mock_walk.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            task_func('/non/existing/directory', self.destination_directory, '*.txt')
    @patch('os.walk')
    @patch('shutil.move')
    def test_case_sensitivity(self, mock_move, mock_walk):
        # Setting up os.walk to simulate case sensitivity in file matching
        mock_walk.return_value = [
            (self.source_directory, [], ['file1.txt', 'file2.TXT', 'report.TXT'])
        ]
        # Execute the function
        task_func(self.source_directory, self.destination_directory, '*.TXT')
        expected_calls = [
            call(os.path.join(self.source_directory, 'file2.TXT'), os.path.join(self.destination_directory, 'file2.TXT')),
            call(os.path.join(self.source_directory, 'report.TXT'), os.path.join(self.destination_directory, 'report.TXT'))
        ]
        mock_move.assert_has_calls(expected_calls, any_order=True)
    @patch('os.walk')
    @patch('shutil.move')
    def test_special_characters_in_filenames(self, mock_move, mock_walk):
        mock_walk.return_value = [(self.source_directory, [], ['config file.cfg'])]
        task_func(self.source_directory, self.destination_directory, '*.cfg')
        expected_call = call(os.path.join(self.source_directory, 'config file.cfg'), os.path.join(self.destination_directory, 'config file.cfg'))
        mock_move.assert_has_calls([expected_call], any_order=True)
    @patch('os.listdir')
    @patch('shutil.move')
    @patch('os.path.exists')
    def test_no_matching_files(self, mock_exists, mock_move, mock_listdir):
        # Setup mocks to simulate no matching files
        mock_listdir.return_value = ['file3.jpg']
        mock_exists.return_value = True
        # Call the function
        moved_files = task_func(self.source_directory, self.destination_directory, '*.txt')
        # Assertions
        mock_move.assert_not_called()
        self.assertEqual(moved_files, [], "No TXT files should be moved")
