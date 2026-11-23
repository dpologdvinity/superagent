from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import tempfile
import os
import shutil

class TestCases(unittest.TestCase):

    def setUp(self):
        self.directory = tempfile.mkdtemp()
        self.backup_directory = tempfile.mkdtemp()

    def tearDown(self):
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        if os.path.exists(self.backup_directory):
            shutil.rmtree(self.backup_directory)

    def test_backup_directory_creation(self):
        """ Test that the backup directory is created if it does not exist. """
        shutil.rmtree(self.backup_directory)
        task_func(self.directory, self.backup_directory)
        self.assertTrue(os.path.exists(self.backup_directory))

    def test_file_copying(self):
        """ Test that files are correctly copied to the backup directory. """
        test_file = os.path.join(self.directory, 'test1.json')
        with open(test_file, 'w') as f:
            f.write('{"test": "data"}')
        task_func(self.directory, self.backup_directory)
        copied_file = os.path.join(self.backup_directory, 'test1.json')
        self.assertTrue(os.path.exists(copied_file))

    def test_json_file_selection(self):
        """ Test that only JSON files are selected for copying. """
        json_file = os.path.join(self.directory, 'test1.json')
        txt_file = os.path.join(self.directory, 'test2.txt')
        with open(json_file, 'w') as f:
            f.write('{"test": "data"}')
        with open(txt_file, 'w') as f:
            f.write('some text')
        result = task_func(self.directory, self.backup_directory)
        self.assertEqual(len(result), 1)
        self.assertTrue('test1.json' in result[0])
