from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import os

class TestCases(unittest.TestCase):

    def test_wrong_keys(self):
        data = {'Names': ['Tom', 'Nick'], 'Ages': [20, 21], 'Scores': [85, 79]}
        with self.assertRaises(ValueError):
            task_func(data)

    def test_correct_processing(self):
        data = {'Name': ['Tom', 'Nick', 'Tom', 'John'], 'Age': [20, 21, 20, 19], 'Score': [85, 79, 88, 92]}
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(df.iloc[0]['Name'], 'John')
        self.assertAlmostEqual(avg_scores['Tom'], 86.5)
        self.assertEqual(common_age, 20)

    def test_empty_data(self):
        data = {'Name': [], 'Age': [], 'Score': []}
        df, avg_scores, common_age = task_func(data)
        self.assertTrue(df.empty)
        self.assertTrue(avg_scores.empty)
        self.assertIsNone(common_age)
