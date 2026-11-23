from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
from zipfile import ZipFile
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test default parameters
        zipped_file = task_func()
        self.assertEqual(zipped_file, "latin_files.zip")
        self.assertTrue(os.path.exists(zipped_file))
        
        # Extract the zipped file and check contents
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("test_case_1")
        self.assertTrue(os.path.exists(os.path.join("latin_files", "file1.txt")))
        self.assertTrue(os.path.exists(os.path.join("latin_files", "file2.txt")))
        self.assertTrue(os.path.exists(os.path.join("latin_files", "file3.txt")))
        for i in range(1,4):
            with open(os.path.join("latin_files", f'file{i}.txt'), encoding='latin-1') as file:
                self.assertEqual(file.read(), 'Sopetón')
        shutil.rmtree("test_case_1")
        os.remove(zipped_file)
        shutil.rmtree("latin_files")
    def test_case_2(self):
        # Test with custom directory and file names
        zipped_file = task_func(directory_name="custom_directory", content='test', file_names=["custom1.txt", "custom2.txt"], encoding='utf-8')
        self.assertEqual(zipped_file, "custom_directory.zip")
        self.assertTrue(os.path.exists(zipped_file))
        
        # Extract the zipped file and check contents
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("test_case_2")
        self.assertTrue(os.path.exists(os.path.join("test_case_2", "custom_directory", "custom1.txt")))
        self.assertTrue(os.path.exists(os.path.join("test_case_2", "custom_directory", "custom2.txt")))
        for i in range(1,3):
            with open(os.path.join("custom_directory", f'custom{i}.txt'), encoding='latin-1') as file:
                self.assertEqual(file.read(), 'test')    
    
        shutil.rmtree("test_case_2")
        os.remove(zipped_file)
        shutil.rmtree("custom_directory")
    def test_case_3(self):
        # Test with custom encoding
        zipped_file = task_func(encoding="utf-8")
        self.assertEqual(zipped_file, "latin_files.zip")
        self.assertTrue(os.path.exists(zipped_file))
        
        # Extract the zipped file and check contents
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("test_case_3")
        with open(os.path.join("test_case_3", "latin_files", "file1.txt"), 'r') as file:
            content = file.read()
        self.assertEqual(content, 'Sopetón')  # Since we used utf-8 encoding, the content should match
        shutil.rmtree("test_case_3")
        os.remove(zipped_file)
        shutil.rmtree("latin_files")
    def test_case_4(self):
        # Test with all custom parameters
        zipped_file = task_func(directory_name="all_custom", file_names=["all1.txt", "all2.txt"], encoding="utf-8")
        self.assertEqual(zipped_file, "all_custom.zip")
        self.assertTrue(os.path.exists(zipped_file))
        
        # Extract the zipped file and check contents
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("test_case_4")
        with open(os.path.join("test_case_4", "all_custom", "all1.txt"), 'r') as file:
            content = file.read()
        self.assertEqual(content, 'Sopetón')  # Since we used utf-8 encoding, the content should match
        shutil.rmtree("test_case_4")
        os.remove(zipped_file)
        shutil.rmtree("all_custom")
    def test_case_5(self):
        # Test with a single file and default encoding
        zipped_file = task_func(directory_name="single_file_dir", file_names=["single.txt"])
        self.assertEqual(zipped_file, "single_file_dir.zip")
        self.assertTrue(os.path.exists(zipped_file))
        
        # Extract the zipped file and check contents
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("test_case_5")
        self.assertTrue(os.path.exists(os.path.join("test_case_5", "single_file_dir", "single.txt")))
        shutil.rmtree("test_case_5")
        shutil.rmtree("single_file_dir")
        os.remove(zipped_file)
