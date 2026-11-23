from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_dir_1 = os.path.join(self.temp_dir, 'test_dir_1')
        self.empty_dir = os.path.join(self.temp_dir, 'empty_dir')
        os.mkdir(self.test_dir_1)
        os.mkdir(self.empty_dir)
        self.create_test_files(self.test_dir_1, ['test1.pdf', 'data.csv', 'image.jpg', 'invalid file name.jpg'])

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def create_test_files(self, directory, filenames):
        for filename in filenames:
            path = os.path.join(directory, filename)
            with open(path, 'w') as f:
                f.write('Dummy content')

    def test_file_moves(self):
        task_func(self.test_dir_1)
        invalid_dir = os.path.join(self.test_dir_1, 'Invalid')
        self.assertTrue(os.path.exists(invalid_dir))
        self.assertEqual(len(os.listdir(invalid_dir)), 4)

    def test_empty_directory(self):
        summary = task_func(self.empty_dir)
        self.assertEqual(summary, {})

    def test_basic_functionality(self):
        summary = task_func(self.test_dir_1)
        expected = {'Invalid': 4}
        self.assertEqual(summary, expected)
