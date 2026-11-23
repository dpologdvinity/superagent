from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import tempfile
import os

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def _create_temp_log_file(self, file_name: str, content: str):
        """Helper function to create a temporary log file."""
        path = os.path.join(self.temp_dir.name, file_name)
        with open(path, 'w') as f:
            f.write(content)
        return path

    def test_case_1(self):
        content = '2023-01-01 12:00:00.000000 - INFO - Application started\n2023-01-01 12:01:00.000000 - ERROR - Failed to connect to database\n'
        log_file_path = self._create_temp_log_file('log1.txt', content)
        df = task_func(log_file_path)
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[0]['Level'], 'INFO')
        self.assertEqual(df.iloc[1]['Level'], 'ERROR')

    def test_case_2(self):
        log_file_path = self._create_temp_log_file('log2.txt', '')
        df = task_func(log_file_path)
        self.assertTrue(df.empty)

    def test_case_3(self):
        content = 'This is not a valid log entry\n2023-01-02 13:00:00.000000 - WARNING - Low disk space\n'
        log_file_path = self._create_temp_log_file('log3.txt', content)
        df = task_func(log_file_path)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Level'], 'WARNING')
