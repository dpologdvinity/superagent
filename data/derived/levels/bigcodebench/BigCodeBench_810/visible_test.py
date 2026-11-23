from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock

class TestCases(unittest.TestCase):

    @patch('os.walk')
    @patch('subprocess.run')
    def test_finding_executable_files(self, mock_run, mock_walk):
        mock_walk.return_value = [(os.path.normpath('C:\\TestDir'), [], ['test_file.exe'])]
        found_files = task_func('C:\\TestDir', 'test_file\\.exe', execute_files=False)
        found_files = [os.path.normpath(path) for path in found_files]
        self.assertEqual(len(found_files), 1)
        self.assertNotIn(os.path.normpath('C:\\TestDir\\test_file.exe'), found_files)

    @patch('os.walk')
    def test_invalid_directory(self, mock_walk):
        mock_walk.return_value = []
        found_files = task_func('C:\\InvalidDir', 'test_pattern', execute_files=False)
        self.assertEqual(found_files, [])

    @patch('os.walk')
    def test_no_matching_files(self, mock_walk):
        mock_walk.return_value = [(os.path.normpath('C:\\TestDir'), [], ['unrelated_file.txt'])]
        found_files = task_func('C:\\TestDir', 'no_match_pattern', execute_files=False)
        self.assertEqual(found_files, [])
