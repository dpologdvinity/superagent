from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
import shutil
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_directory = f"{self.base_tmp_dir}/test"
        self.mixed_directory = f"{self.base_tmp_dir}/test/mixed_directory/"
        if not os.path.exists(self.test_directory):
            os.makedirs(self.test_directory)
        if not os.path.exists(self.mixed_directory):
            os.makedirs(self.mixed_directory)
        self.json_data1 = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.json_data2 = {
            "book": "Harry Potter",
            "author": "J.K. Rowling",
            "quote": "\"Magic\" is everywhere!"
        }
        # Create sample JSON files
        with open(os.path.join(self.test_directory, "file1.json"), "w") as file:
            json.dump(self.json_data1, file)
        with open(os.path.join(self.test_directory, "file2.json"), "w") as file:
            json.dump(self.json_data2, file)
    def tearDown(self):
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)
    def test_case_1(self):
        # Test with the sample directory created
        result = task_func(self.test_directory)
        self.assertEqual(len(result), 2)  # 2 files processed
        result = [os.path.basename(file) for file in result]
        self.assertTrue("file1.json" in result)
        self.assertTrue("file2.json" in result)
        
        # Check if the files have been modified correctly
        with open(os.path.join(self.test_directory, "file1.json"), "r") as file:
            content = file.read()
            self.assertNotIn(' "', content)  # No unprotected double quotes
        
        with open(os.path.join(self.test_directory, "file2.json"), "r") as file:
            content = file.read()
            self.assertNotIn(' "Magic"', content)  # Original quote should be escaped
    
    def test_case_2(self):
        # Test with an empty directory (no JSON files)
        empty_directory = f"{self.test_directory}/empty_directory/"
        if not os.path.exists(empty_directory):
            os.makedirs(empty_directory)
        result = task_func(empty_directory)
        self.assertEqual(result, [])  # No files processed
    
    def test_case_3(self):
        # Test with a non-existing directory
        with self.assertRaises(FileNotFoundError):
            task_func("/mnt/data/non_existent_directory/")
    
    def test_case_4(self):
        # Test with a directory containing non-JSON files
        if not os.path.exists(self.mixed_directory):
            os.makedirs(self.mixed_directory)
        with open(self.mixed_directory + "file.txt", "w") as file:
            file.write("Sample text")
        result = task_func(self.mixed_directory)
        self.assertEqual(result, [])  # No JSON files processed
    
    def test_case_5(self):
        # Test with a directory containing both JSON and non-JSON files
        with open(self.mixed_directory + "file3.json", "w") as file:
            json.dump(self.json_data1, file)
        result = task_func(self.mixed_directory)
        self.assertEqual(len(result), 1)  # 1 JSON file processed
        self.assertTrue("file3.json" in result[0])
