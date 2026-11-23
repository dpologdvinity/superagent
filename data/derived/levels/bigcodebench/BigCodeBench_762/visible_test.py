from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
from zipfile import ZipFile

class TestCases(unittest.TestCase):

    def test_case_1(self):
        zipped_file = task_func()
        self.assertEqual(zipped_file, 'latin_files.zip')
        self.assertTrue(os.path.exists(zipped_file))
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall('test_case_1')
        self.assertTrue(os.path.exists(os.path.join('latin_files', 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join('latin_files', 'file2.txt')))
        self.assertTrue(os.path.exists(os.path.join('latin_files', 'file3.txt')))
        for i in range(1, 4):
            with open(os.path.join('latin_files', f'file{i}.txt'), encoding='latin-1') as file:
                self.assertEqual(file.read(), 'Sopetón')
        shutil.rmtree('test_case_1')
        os.remove(zipped_file)
        shutil.rmtree('latin_files')

    def test_case_2(self):
        zipped_file = task_func(directory_name='custom_directory', content='test', file_names=['custom1.txt', 'custom2.txt'], encoding='utf-8')
        self.assertEqual(zipped_file, 'custom_directory.zip')
        self.assertTrue(os.path.exists(zipped_file))
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall('test_case_2')
        self.assertTrue(os.path.exists(os.path.join('test_case_2', 'custom_directory', 'custom1.txt')))
        self.assertTrue(os.path.exists(os.path.join('test_case_2', 'custom_directory', 'custom2.txt')))
        for i in range(1, 3):
            with open(os.path.join('custom_directory', f'custom{i}.txt'), encoding='latin-1') as file:
                self.assertEqual(file.read(), 'test')
        shutil.rmtree('test_case_2')
        os.remove(zipped_file)
        shutil.rmtree('custom_directory')

    def test_case_3(self):
        zipped_file = task_func(encoding='utf-8')
        self.assertEqual(zipped_file, 'latin_files.zip')
        self.assertTrue(os.path.exists(zipped_file))
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall('test_case_3')
        with open(os.path.join('test_case_3', 'latin_files', 'file1.txt'), 'r') as file:
            content = file.read()
        self.assertEqual(content, 'Sopetón')
        shutil.rmtree('test_case_3')
        os.remove(zipped_file)
        shutil.rmtree('latin_files')
