from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import os
def create_dummy_files(data_dir):
    os.makedirs(data_dir, exist_ok=True)
    # Creating dummy CSV files with more diverse data
    dummy_files = ['test1.csv', 'test2.csv']
    # Create a DataFrame with a range of integers
    pd.DataFrame({'col1': range(5), 'col2': range(5, 10)}).to_csv(data_dir + dummy_files[0], index=False)
    # Create a DataFrame with mixed data types and missing values
    mixed_data = pd.DataFrame({
        'a': range(10),
        'b': [float(x) for x in range(10)],
        'c': list('abcdefghij'),
        'd': [None if x % 2 == 0 else x for x in range(10)]
    })
    mixed_data.to_csv(data_dir + dummy_files[1], index=False)
    return dummy_files
def tear_down_dummy_files(data_dir, dummy_files):
    # Cleaning up the dummy data directory
    for file in dummy_files:
        os.remove(data_dir + file)
    os.rmdir(data_dir)
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setting up a dummy data directory
        self.test_data_dir = './test_data/'
        os.makedirs(self.test_data_dir, exist_ok=True)
        # Creating dummy CSV files with more diverse data
        self.dummy_files = ['test1.csv', 'test2.csv', 'empty.csv']
        # Create a DataFrame with a range of integers
        pd.DataFrame({'col1': range(5), 'col2': range(5, 10)}).to_csv(self.test_data_dir + self.dummy_files[0], index=False)
        # Create a DataFrame with mixed data types and missing values
        mixed_data = pd.DataFrame({
            'a': range(10),
            'b': [float(x) for x in range(10)],
            'c': list('abcdefghij'),
            'd': [None if x % 2 == 0 else x for x in range(10)]
        })
        mixed_data.to_csv(self.test_data_dir + self.dummy_files[1], index=False)
        # Empty DataFrame for the third file
        pd.DataFrame().to_csv(self.test_data_dir + self.dummy_files[2], index=False)
    def tearDown(self):
        for file in self.dummy_files:
            file_path = os.path.join(self.test_data_dir, file)
            if os.path.exists(file_path):
                os.remove(file_path)
        if os.path.exists(self.test_data_dir):
            os.rmdir(self.test_data_dir)
    def test_normal_functionality(self):
        os.remove(self.test_data_dir + 'empty.csv')
        table_str = task_func(self.test_data_dir)
        with open('df_contents.txt', 'w') as file:
            file.write(str(table_str))
            
        expect_str = '''+-----------+------+---------+
|   File    | Rows | Columns |
+===========+======+=========+
| test1.csv | 5    | 2       |
+-----------+------+---------+
| test1.csv | 5    | 2       |
+-----------+------+---------+
| test2.csv | 10   | 4       |
+-----------+------+---------+
| test2.csv | 10   | 4       |
+-----------+------+---------+'''
        self.assertEqual(expect_str, table_str)
        pd.DataFrame().to_csv(self.test_data_dir + 'empty.csv', index=False)
        
    def test_directory_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            task_func('./nonexistent_directory/')
    def test_no_csv_files(self):
        with self.assertRaises(ValueError):
            empty_dir = './empty_test_data/'
            os.makedirs(empty_dir, exist_ok=True)
            task_func(empty_dir)
            os.rmdir(empty_dir)
    def test_empty_csv_file(self):
        with self.assertRaises(pd.errors.EmptyDataError):
            task_func(self.test_data_dir)
    def test_file_path_in_output(self):
        # Temporarily remove the empty CSV file
        os.remove(self.test_data_dir + 'empty.csv')
        table_str = task_func(self.test_data_dir)
        for file in self.dummy_files:
            if file != 'empty.csv':  # Skip the empty file
                self.assertIn(file, table_str)
        # Restore the empty CSV file
        pd.DataFrame().to_csv(self.test_data_dir + 'empty.csv', index=False)
