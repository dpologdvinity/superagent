from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock, call
import os
import shutil
source_dirs = ['/mnt/data/test_data/source_0', '/mnt/data/test_data/source_1', '/mnt/data/test_data/source_2', '/mnt/data/test_data/source_3', '/mnt/data/test_data/source_4']
target_dirs = ['/mnt/data/test_data/target_0', '/mnt/data/test_data/target_1', '/mnt/data/test_data/target_2', '/mnt/data/test_data/target_3', '/mnt/data/test_data/target_4']

class TestCases(unittest.TestCase):

    @patch('os.listdir')
    @patch('shutil.move')
    @patch('os.path.join', side_effect=lambda *args: '/'.join(args))
    def test_move_json_files(self, mock_join, mock_move, mock_listdir):
        mock_listdir.return_value = ['data-1.json', 'info-2.json', 'report-3.json']
        task_func()
        expected_calls = [call('/source/dir/data-1.json', '/target/dir/data.json'), call('/source/dir/info-2.json', '/target/dir/info.json'), call('/source/dir/report-3.json', '/target/dir/report.json')]
        mock_move.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir', MagicMock(return_value=[]))
    @patch('shutil.move')
    def test_no_files_to_move(self, mock_move):
        task_func()
        mock_move.assert_not_called()

    @patch('os.listdir', return_value=['wrongfile.txt', 'not-a-json-1.txt', 'badname.json'])
    @patch('shutil.move')
    def test_incorrect_file_patterns(self, mock_move, mock_listdir):
        task_func()
        mock_move.assert_not_called()
