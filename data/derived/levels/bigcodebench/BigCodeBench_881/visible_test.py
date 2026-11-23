from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import tempfile
import shutil
import os

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, 'test_data.csv')
        data = {'data': ['123x good', 'no match here', '456X bad', '789x good', 'ABC'], 'other_column': ['data1', 'data2', 'data3', 'data4', 'data5']}
        self.df = pd.DataFrame(data)
        self.df.to_csv(self.test_file, index=False)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_default_parameters(self):
        result = task_func(self.test_file)
        expected_data = {'data': ['123x good', '456X bad', '789x good'], 'other_column': ['data1', 'data3', 'data4']}
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

    def test_custom_column(self):
        with self.assertRaises(KeyError):
            task_func(self.test_file, column_name='nonexistent_column')

    def test_custom_pattern(self):
        result = task_func(self.test_file, pattern='\\d+X')
        expected_data = {'data': ['456X bad'], 'other_column': ['data3']}
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)
