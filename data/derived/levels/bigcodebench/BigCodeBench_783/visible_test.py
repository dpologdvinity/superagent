from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import os
import shutil
import tempfile
import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        self.src_dir = tempfile.mkdtemp()
        self.dest_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.src_dir)
        shutil.rmtree(self.dest_dir)

    def test_case_1(self):
        file_names = ['file1.txt', 'file2.txt', 'file3.doc', 'file4.txt', 'file5.png']
        for fname in file_names:
            open(os.path.join(self.src_dir, fname), 'a').close()
        moved_files_count = task_func(self.src_dir, self.dest_dir, '.txt')
        self.assertEqual(moved_files_count, 3)

    def test_case_2(self):
        file_names = ['file1.doc', 'file2.doc', 'file3.doc', 'file4.doc']
        for fname in file_names:
            open(os.path.join(self.src_dir, fname), 'a').close()
        moved_files_count = task_func(self.src_dir, self.dest_dir, '.doc')
        self.assertEqual(moved_files_count, 4)

    def test_case_3(self):
        file_names = ['file1.png', 'file2.jpg', 'file3.jpeg']
        for fname in file_names:
            open(os.path.join(self.src_dir, fname), 'a').close()
        moved_files_count = task_func(self.src_dir, self.dest_dir, '.txt')
        self.assertEqual(moved_files_count, 0)
