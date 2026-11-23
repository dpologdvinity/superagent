from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import os
import tempfile
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.test_files = [
            'file1.csv', 'file2.csv', 'file3.csv', 'file4.csv', 'file5.csv', 'empty.csv'
        ]
        # Sample data for CSV files
        data = {
            'file1.csv': pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]}),
            'file2.csv': pd.DataFrame({'Name': ['Chris', 'Dana'], 'Age': [35, 40]}),
            'file3.csv': pd.DataFrame({'Name': ['Eve', 'Frank'], 'Age': [45, 50]}),
            'file4.csv': pd.DataFrame({'Name': ['Grace', 'Hank'], 'Age': [55, 60]}),
            'file5.csv': pd.DataFrame({'Name': ['Ivan', 'Julia'], 'Age': [65, 70]}),
            'empty.csv': pd.DataFrame()
        }
        # Create CSV files in the directory
        for file_name, df in data.items():
            df.to_csv(os.path.join(self.test_dir, file_name), index=False)
    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)
    def test_random_selection(self):
        # Testing random selection and ensuring the file chosen and its data are correct
        file_name, df = task_func(self.test_dir, seed=42)
        self.assertTrue(file_name in self.test_files)
        self.assertFalse(df.empty)
    def test_specific_file_selection(self):
        # Test selecting a specific file and checking contents
        file_name, df = task_func(self.test_dir, ['file1.csv'], seed=42)
        expected = pd.read_csv(os.path.join(self.test_dir, 'file1.csv'))
        # Sample from expected and reset index
        expected_sampled = expected.sample(len(df), random_state=42).reset_index(drop=True)
        # Reset index of df to ensure indices match
        df_reset = df.reset_index(drop=True)
        # Assert frame equality
        pd.testing.assert_frame_equal(df_reset, expected_sampled)
    def test_empty_file(self):
        # Ensure an empty file returns an empty DataFrame
        file_name, df = task_func(self.test_dir, ['empty.csv'], seed=42)
        self.assertEqual(file_name, 'empty.csv')
        self.assertTrue(df.empty)
    def test_multiple_files(self):
        # Testing selection from multiple files
        file_name, df = task_func(self.test_dir, ['file3.csv', 'file4.csv'], seed=24)
        self.assertIn(file_name, ['file3.csv', 'file4.csv'])
        self.assertFalse(df.empty)
    def test_no_file_matches(self):
        # Testing behavior when no files match the list
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_dir, ['nonexistent.csv'], seed=42)
