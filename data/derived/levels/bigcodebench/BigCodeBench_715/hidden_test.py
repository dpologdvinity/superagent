from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import sys
import unittest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    @patch('subprocess.run')
    def test_switch_to_default_python_version(self, mock_run):
        original_path_length = len(sys.path)
        task_func()
        mock_run.assert_called_with(['pyenv', 'global', '3.8'], check=True)
        self.assertEqual(sys.path[-1], '/path/to/whatever')
        sys.path = sys.path[:original_path_length]  # Reset sys.path to original state
    @patch('subprocess.run')
    def test_switch_to_python_3_7(self, mock_run):
        original_path_length = len(sys.path)
        task_func('3.7', '/another/path')
        mock_run.assert_called_with(['pyenv', 'global', '3.7'], check=True)
        self.assertEqual(sys.path[-1], '/another/path')
        sys.path = sys.path[:original_path_length]
    @patch('subprocess.run')
    def test_switch_to_python_3_9(self, mock_run):
        original_path_length = len(sys.path)
        task_func('3.9')
        mock_run.assert_called_with(['pyenv', 'global', '3.9'], check=True)
        self.assertEqual(sys.path[-1], '/path/to/whatever')
        sys.path = sys.path[:original_path_length]
    @patch('subprocess.run')
    def test_switch_to_python_2_7(self, mock_run):
        original_path_length = len(sys.path)
        task_func('2.7')
        mock_run.assert_called_with(['pyenv', 'global', '2.7'], check=True)
        self.assertEqual(sys.path[-1], '/path/to/whatever')
        sys.path = sys.path[:original_path_length]
    @patch('subprocess.run')
    def test_switch_to_python_3_6(self, mock_run):
        original_path_length = len(sys.path)
        task_func('3.6', '/different/path')
        mock_run.assert_called_with(['pyenv', 'global', '3.6'], check=True)
        self.assertEqual(sys.path[-1], '/different/path')
        sys.path = sys.path[:original_path_length]
