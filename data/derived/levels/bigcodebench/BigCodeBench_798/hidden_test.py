from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock
import os
import shutil
class TestCases(unittest.TestCase):
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.rmtree')
    @patch('shutil.copytree')
    def test_successful_rollback(self, mock_copytree, mock_rmtree, mock_exists, mock_listdir):
        mock_exists.side_effect = lambda x: True if x == BACKUP_DIR else False
        mock_listdir.return_value = ['backup1']
        result = task_func('/tmp/my_data')
        self.assertEqual(result, '/tmp/my_data')
        mock_copytree.assert_called_once()
    @patch('os.listdir')
    @patch('os.path.exists')
    def test_no_backup_directory(self, mock_exists, mock_listdir):
        mock_exists.return_value = False
        result = task_func('/tmp/my_data')
        self.assertEqual(result, 'Backup directory /tmp/backup does not exist. Cannot rollback update.')
    @patch('os.listdir')
    @patch('os.path.exists')
    def test_no_backups_in_backup_directory(self, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = []
        result = task_func('/tmp/my_data')
        self.assertEqual(result, 'No backups found in /tmp/backup. Cannot rollback update.')
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.rmtree')
    @patch('shutil.copytree')
    def test_directory_does_not_exist(self, mock_copytree, mock_rmtree, mock_exists, mock_listdir):
        mock_exists.side_effect = lambda x: True if x == BACKUP_DIR else False
        mock_listdir.return_value = ['backup1']
        result = task_func('/tmp/nonexistent')
        self.assertEqual(result, '/tmp/nonexistent')
        mock_copytree.assert_called_once()
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.rmtree')
    @patch('shutil.copytree')
    def test_erroneous_backup_content(self, mock_copytree, mock_rmtree, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = ['corrupt_backup']
        mock_copytree.side_effect = Exception("Corruption detected")
        with self.assertRaises(Exception) as context:
            task_func('/tmp/my_data')
        self.assertTrue('Corruption detected' in str(context.exception))
