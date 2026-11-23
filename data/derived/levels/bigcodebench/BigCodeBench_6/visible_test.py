from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import os
import re

class TestCases(unittest.TestCase):

    @patch('os.listdir')
    @patch('os.path.getmtime')
    def test_case_1(self, mock_getmtime, mock_listdir):
        mock_listdir.return_value = ['file1.txt', 'file2.log', 'access.log.abc']
        result = task_func('^access.log.[0-9]+$', '/mock_dir/')
        self.assertIsNone(result)

    @patch('os.listdir')
    @patch('os.path.getmtime')
    def test_case_2(self, mock_getmtime, mock_listdir):
        mock_listdir.return_value = ['access.log.1', 'access.log.2', 'access.log.3']
        mock_getmtime.side_effect = [3, 1, 2]
        result = task_func('^access.log.[0-9]+$', '/mock_dir/')
        self.assertEqual(result, '/mock_dir/access.log.1')

    @patch('os.listdir')
    @patch('os.path.getmtime')
    def test_case_3(self, mock_getmtime, mock_listdir):
        mock_listdir.return_value = ['file1.txt', 'file2.log', 'access.log.123']
        mock_getmtime.return_value = 1
        result = task_func('^access.log.[0-9]+$', '/mock_dir/')
        self.assertEqual(result, '/mock_dir/access.log.123')
