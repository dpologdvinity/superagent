from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import tempfile
import shutil

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, 'test.txt')
        with open(self.test_file, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_copy_and_erase(self):
        dest_dir = os.path.join(self.test_dir, 'dest')
        copied_file = task_func(self.test_file, dest_dir)
        self.assertTrue(os.path.isfile(copied_file))
        with open(self.test_file, 'r') as f:
            self.assertEqual(f.read(), '')

    def test_non_existent_dest_dir(self):
        dest_dir = os.path.join(self.test_dir, 'non_existent_dir')
        copied_file = task_func(self.test_file, dest_dir)
        self.assertTrue(os.path.isdir(dest_dir))
        self.assertTrue(os.path.isfile(copied_file))

    def test_overwrite_existing_file(self):
        dest_dir = os.path.join(self.test_dir, 'dest')
        os.makedirs(dest_dir, exist_ok=True)
        existing_file_path = os.path.join(dest_dir, 'test.txt')
        with open(existing_file_path, 'w') as f:
            f.write('Old content')
        copied_file = task_func(self.test_file, dest_dir)
        with open(copied_file, 'r') as f:
            self.assertEqual(f.read(), 'This is a test file.')
