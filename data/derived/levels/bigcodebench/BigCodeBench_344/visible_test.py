from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import tempfile
import doctest

class TestCases(unittest.TestCase):

    def setUp(self):
        self.src_folder = tempfile.mkdtemp()
        self.backup_dir = tempfile.mkdtemp()
        with open(os.path.join(self.src_folder, 'sample.txt'), 'w') as f:
            f.write('This is a sample file.')

    def tearDown(self):
        if os.path.exists(self.src_folder):
            shutil.rmtree(self.src_folder)
        if os.path.exists(self.backup_dir):
            shutil.rmtree(self.backup_dir)

    def test_case_1(self):
        result = task_func(self.src_folder, self.backup_dir)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(self.src_folder))
        self.assertTrue(os.path.exists(os.path.join(self.backup_dir, os.path.basename(self.src_folder), 'sample.txt')))

    def test_case_2(self):
        shutil.rmtree(self.src_folder)
        with self.assertRaises(ValueError):
            task_func(self.src_folder, self.backup_dir)

    def test_case_3(self):
        os.rmdir(self.backup_dir)
        result = task_func(self.src_folder, self.backup_dir)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(self.src_folder))
        self.assertTrue(os.path.exists(os.path.join(self.backup_dir, os.path.basename(self.src_folder), 'sample.txt')))
