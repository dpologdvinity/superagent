from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import tempfile
import unittest

class TestCases(unittest.TestCase):

    def create_test_file(self, directory, filename, age_days):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'w') as f:
            f.write('Test content')
        old_time = time.time() - age_days * 86400
        os.utime(file_path, (old_time, old_time))
        return file_path

    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            archive_dir = task_func(tmpdir, 30)
            self.assertTrue(os.path.isdir(archive_dir), 'Archive directory not created')
            self.assertEqual(len(os.listdir(archive_dir)), 0, 'Archive directory is not empty')

    def test_no_old_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            self.create_test_file(tmpdir, 'test1.txt', 10)
            archive_dir = task_func(tmpdir, 30)
            self.assertTrue(os.path.isdir(archive_dir), 'Archive directory not created')
            self.assertEqual(len(os.listdir(archive_dir)), 0, 'Old files incorrectly archived')

    def test_old_files_archived(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            old_file = self.create_test_file(tmpdir, 'test2.txt', 40)
            archive_dir = task_func(tmpdir, 30)
            self.assertTrue(os.path.isfile(os.path.join(archive_dir, 'test2.txt')), 'Old file not archived')
