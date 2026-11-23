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
        # Testing with .txt files to ensure correct number of .txt files are moved
        file_names = ["file1.txt", "file2.txt", "file3.doc", "file4.txt", "file5.png"]
        for fname in file_names:
            open(os.path.join(self.src_dir, fname), 'a').close()
        moved_files_count = task_func(self.src_dir, self.dest_dir, ".txt")
        self.assertEqual(moved_files_count, 3)
    def test_case_2(self):
        # Testing with .doc files to ensure correct number of .doc files are moved
        file_names = ["file1.doc", "file2.doc", "file3.doc", "file4.doc"]
        for fname in file_names:
            open(os.path.join(self.src_dir, fname), 'a').close()
        moved_files_count = task_func(self.src_dir, self.dest_dir, ".doc")
        self.assertEqual(moved_files_count, 4)
    def test_case_3(self):
        # Testing with no matching files to ensure zero files are moved
        file_names = ["file1.png", "file2.jpg", "file3.jpeg"]
        for fname in file_names:
            open(os.path.join(self.src_dir, fname), 'a').close()
        moved_files_count = task_func(self.src_dir, self.dest_dir, ".txt")
        self.assertEqual(moved_files_count, 0)
    def test_case_4(self):
        # Testing with empty source directory to ensure zero files are moved
        moved_files_count = task_func(self.src_dir, self.dest_dir, ".txt")
        self.assertEqual(moved_files_count, 0)
    def test_case_5(self):
        # Testing with mixed file extensions to ensure correct number of .txt files are moved
        file_names = ["file1.txt", "file2.txt", "file3.doc", "file4.jpeg", "file5.txt", "file6.png"]
        for fname in file_names:
            open(os.path.join(self.src_dir, fname), 'a').close()
        moved_files_count = task_func(self.src_dir, self.dest_dir, ".txt")
        self.assertEqual(moved_files_count, 3)
