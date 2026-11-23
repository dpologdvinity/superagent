from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_dir = 'temp_test_dir'
        os.makedirs(self.temp_dir, exist_ok=True)

    def test_rng(self):
        """test rng reproducability"""
        df1 = task_func(300, file_path=os.path.join(self.temp_dir, 'test1.csv'), random_seed=42)
        df1_from_csv = pd.read_csv(os.path.join(self.temp_dir, 'test1.csv'))
        df2 = task_func(300, file_path=os.path.join(self.temp_dir, 'test2.csv'), random_seed=42)
        df2_from_csv = pd.read_csv(os.path.join(self.temp_dir, 'test2.csv'))
        self.assertTrue(pd.testing.assert_frame_equal(df1, df2) is None)
        self.assertTrue(pd.testing.assert_frame_equal(df1_from_csv, df1) is None)
        self.assertTrue(pd.testing.assert_frame_equal(df2_from_csv, df2) is None)

    def test_case_1(self):
        n = 100
        df = task_func(n, file_path=os.path.join(self.temp_dir, 'test1.csv'), random_seed=1)
        df_from_csv = pd.read_csv(os.path.join(self.temp_dir, 'test1.csv'))
        self.assertTrue(pd.testing.assert_frame_equal(df_from_csv, df) is None)
        self.assertEqual(len(df), n)
        self.assertTrue(set(df['Site'].unique()).issubset(set(['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'])))
        self.assertTrue(set(df['Category'].unique()).issubset(set(['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'])))
        self.assertTrue(set(df['Response'].unique()).issubset(set(['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'])))
        self.assertTrue(set(df['Value'].unique()).issubset(set(range(1, 6))))

    def test_case_2(self):
        n = 500
        categories = ['Science', 'Math']
        df = task_func(n, categories=categories, file_path=os.path.join(self.temp_dir, 'test2.csv'), random_seed=12)
        df_from_csv = pd.read_csv(os.path.join(self.temp_dir, 'test2.csv'))
        self.assertTrue(pd.testing.assert_frame_equal(df_from_csv, df) is None)
        self.assertEqual(len(df), n)
        self.assertTrue(set(df['Category'].unique()).issubset(set(categories)))

    def tearDown(self):
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)
