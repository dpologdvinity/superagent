from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_rng(self):
        """test rng reproducability"""
        df1 = task_func(300, random_seed=42)
        df2 = task_func(300, random_seed=42)
        self.assertTrue(pd.testing.assert_frame_equal(df1, df2) is None)

    def test_case_1(self):
        """default params"""
        df = task_func(400, random_seed=10)
        self.assertEqual(len(df), 400)
        self.assertTrue(df['title_url'].str.startswith('samplewebsite.com/Article_').all())
        self.assertEqual(len(df['id'].unique()), 400)
        self.assertTrue(df['category'].isin(['Sports', 'Technology', 'Health', 'Science', 'Business']).all())
        self.assertTrue(df['views'].dtype, int)

    def test_case_2(self):
        """custom params"""
        df = task_func(330, domain='testdomain.com', categories=['A', 'B', 'C'])
        self.assertEqual(len(df), 330)
        self.assertTrue(df['title_url'].str.startswith('testdomain.com/Article_').all())
        self.assertEqual(len(df['id'].unique()), 330)
        self.assertTrue(df['category'].isin(['A', 'B', 'C']).all())
        self.assertTrue(df['views'].dtype, int)
