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
        self.test_dir = tempfile.mkdtemp()
        self.test_files = ['file1.csv', 'file2.csv', 'file3.csv', 'file4.csv', 'file5.csv', 'empty.csv']
        data = {'file1.csv': pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]}), 'file2.csv': pd.DataFrame({'Name': ['Chris', 'Dana'], 'Age': [35, 40]}), 'file3.csv': pd.DataFrame({'Name': ['Eve', 'Frank'], 'Age': [45, 50]}), 'file4.csv': pd.DataFrame({'Name': ['Grace', 'Hank'], 'Age': [55, 60]}), 'file5.csv': pd.DataFrame({'Name': ['Ivan', 'Julia'], 'Age': [65, 70]}), 'empty.csv': pd.DataFrame()}
        for file_name, df in data.items():
            df.to_csv(os.path.join(self.test_dir, file_name), index=False)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_random_selection(self):
        file_name, df = task_func(self.test_dir, seed=42)
        self.assertTrue(file_name in self.test_files)
        self.assertFalse(df.empty)

    def test_specific_file_selection(self):
        file_name, df = task_func(self.test_dir, ['file1.csv'], seed=42)
        expected = pd.read_csv(os.path.join(self.test_dir, 'file1.csv'))
        expected_sampled = expected.sample(len(df), random_state=42).reset_index(drop=True)
        df_reset = df.reset_index(drop=True)
        pd.testing.assert_frame_equal(df_reset, expected_sampled)

    def test_empty_file(self):
        file_name, df = task_func(self.test_dir, ['empty.csv'], seed=42)
        self.assertEqual(file_name, 'empty.csv')
        self.assertTrue(df.empty)
