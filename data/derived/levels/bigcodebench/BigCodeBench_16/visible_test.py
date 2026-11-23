from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import tempfile
import os
import subprocess
import glob
import shutil

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.temp_backup_dir = tempfile.mkdtemp()
        for i in range(5):
            with open(os.path.join(self.temp_dir, f'file_{i}.log'), 'w') as f:
                f.write(f'Mock log content for file_{i}')
            with open(os.path.join(self.temp_dir, f'file_{i}.txt'), 'w') as f:
                f.write(f'Mock content for file_{i}.txt')

    def tearDown(self):
        shutil.rmtree(self.temp_dir)
        shutil.rmtree(self.temp_backup_dir)

    def test_backup_creation_and_log_file_deletion(self):
        backup_path = task_func(self.temp_dir, self.temp_backup_dir)
        self.assertTrue(os.path.exists(backup_path))
        self.assertEqual(backup_path, os.path.join(self.temp_backup_dir, 'logs_backup.tar.gz'))
        self.assertFalse(any((file.endswith('.log') for file in os.listdir(self.temp_dir))))

    def test_no_log_files_to_backup(self):
        empty_dir = tempfile.mkdtemp()
        result = task_func(empty_dir, self.temp_backup_dir)
        self.assertEqual(result, 'No logs found to backup.')
        shutil.rmtree(empty_dir)

    def test_non_log_files_remain(self):
        backup_path = task_func(self.temp_dir, self.temp_backup_dir)
        self.assertEqual(len(glob.glob(os.path.join(self.temp_dir, '*.txt'))), 5)
