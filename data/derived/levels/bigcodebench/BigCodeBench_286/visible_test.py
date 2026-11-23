from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock
from collections import Counter
from faker import Faker
import shutil

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_directory = './testdir_f270'
        os.makedirs(self.test_directory, exist_ok=True)
        self.output_file = 'test_output.csv'
        self.list_files = []

    def create_fake_dict_files(self, directory, num_files, num_words):
        fake = Faker()
        for _ in range(num_files):
            file_name = fake.file_name(extension='txt')
            self.list_files.append(os.path.join(directory, file_name))
            with open(os.path.join(directory, file_name), 'w') as file:
                words = [fake.word() for _ in range(num_words)]
                file.write(' '.join(words))

    def remove_files(self):
        for fn in self.list_files:
            if os.path.exists(fn):
                os.remove(fn)
        self.list_files = []

    def tearDown(self):
        if os.path.exists('test_output.csv'):
            os.remove('test_output.csv')
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)

    def test_no_files_in_directory(self):
        self.create_fake_dict_files(self.test_directory, 0, 0)
        result = task_func(self.output_file, self.test_directory)
        self.assertEqual(result, 0)
        self.remove_files()

    def test_single_file_multiple_words(self):
        self.create_fake_dict_files(self.test_directory, 1, 50)
        result = task_func(self.output_file, self.test_directory)
        self.assertEqual(50, result)
        self.remove_files()

    def test_multiple_files_multiple_words(self):
        self.create_fake_dict_files(self.test_directory, 5, 20)
        result = task_func(self.output_file, self.test_directory)
        self.remove_files()
        self.assertEqual(100, result)
