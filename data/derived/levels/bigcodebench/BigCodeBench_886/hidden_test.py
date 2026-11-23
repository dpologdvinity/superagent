from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import os
class TestCases(unittest.TestCase):
    def test_wrong_keys(self):
        # Testing with incorrect dictionary keys
        data = {
            'Names': ['Tom', 'Nick'],
            'Ages': [20, 21],
            'Scores': [85, 79]
        }
        with self.assertRaises(ValueError):
            task_func(data)
    def test_correct_processing(self):
        # Testing with correctly formatted data
        data = {
            'Name': ['Tom', 'Nick', 'Tom', 'John'],
            'Age': [20, 21, 20, 19],
            'Score': [85, 79, 88, 92]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(df.iloc[0]['Name'], 'John')
        self.assertAlmostEqual(avg_scores['Tom'], 86.5)
        self.assertEqual(common_age, 20)
    def test_empty_data(self):
        # Testing with empty lists
        data = {'Name': [], 'Age': [], 'Score': []}
        df, avg_scores, common_age = task_func(data)
        self.assertTrue(df.empty)
        self.assertTrue(avg_scores.empty)
        self.assertIsNone(common_age)
    def test_all_same_age(self):
        # Testing with all students having the same age
        data = {
            'Name': ['Alice', 'Bob', 'Cindy'],
            'Age': [25, 25, 25],
            'Score': [88, 92, 85]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(common_age, 25)
    def test_no_common_age(self):
        # Testing with no common age, each student has a unique age
        data = {
            'Name': ['Alice', 'Bob', 'Cindy'],
            'Age': [24, 25, 26],
            'Score': [88, 92, 85]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(common_age, 24)  # Assuming the first element is taken if all are equally common
    def test_duplicate_names_different_ages(self):
        # Testing with duplicate names but different ages
        data = {
            'Name': ['Tom', 'Tom', 'Nick'],
            'Age': [20, 21, 21],
            'Score': [85, 88, 79]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(len(df[df['Name'] == 'Tom']), 2)
        self.assertNotEqual(df.iloc[0]['Age'], df.iloc[1]['Age'])
        self.assertTrue(df[df['Name'] == 'Tom'].Age.isin([20, 21]).all())
