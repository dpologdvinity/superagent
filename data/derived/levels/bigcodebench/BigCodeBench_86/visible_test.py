from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def setUp(self):
        self.students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

    def test_random_reproducibility(self):
        df1, _ = task_func(self.students, 42)
        df2, _ = task_func(self.students, 42)
        pd.testing.assert_frame_equal(df1, df2)

    def test_dataframe_columns(self):
        df, _ = task_func(self.students)
        self.assertListEqual(list(df.columns), ['Student', 'Score'])

    def test_scores_within_range(self):
        df, _ = task_func(self.students)
        self.assertTrue(df['Score'].between(0, 100).all())
