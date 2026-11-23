from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    def test_case_1(self):
        text = 'Score: 85, Category: Math\nScore: 90, Category: Science\nScore: 80, Category: Math'
        df = task_func(text)
        self.assertEqual(len(df), 3)
        self.assertEqual(df['Score'].iloc[0], 85)
        self.assertEqual(df['Category'].iloc[0], 'Math')
        self.assertEqual(df['Score'].iloc[1], 90)
        self.assertEqual(df['Category'].iloc[1], 'Science')
        self.assertEqual(df['Score'].iloc[2], 80)
        self.assertEqual(df['Category'].iloc[2], 'Math')

    def test_case_2(self):
        text = 'Score: 70, Category: History'
        df = task_func(text)
        self.assertEqual(len(df), 1)
        self.assertEqual(df['Score'].iloc[0], 70)
        self.assertEqual(df['Category'].iloc[0], 'History')

    def test_case_3(self):
        text = ''
        df = task_func(text)
        self.assertEqual(len(df), 0)
