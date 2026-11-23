from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_dataframe_structure(self):
        students = ['Alice', 'Bob']
        subjects = ['Math', 'Physics']
        report = task_func(students, subjects, seed=42)
        
        # Check if the output is a DataFrame
        self.assertIsInstance(report, pd.DataFrame)
        
        # Check the structure of the DataFrame
        expected_columns = ['Student'] + subjects + ['Average Grade']
        self.assertEqual(list(report.columns), expected_columns)
    def test_average_grade_calculation(self):
        students = ['Alice']
        subjects = ['Math', 'Physics']
        report = task_func(students, subjects, seed=42)
        # Since we know the seed, we know the grades. Let's check the average.
        alice_grades = report.iloc[0, 1:-1]
        self.assertEqual(report.at[0, 'Average Grade'], alice_grades.mean())
    def test_varying_input_sizes(self):
        # Testing with different numbers of students and subjects
        students = ['Alice', 'Bob', 'Charlie']
        subjects = ['Math', 'Physics', 'Biology', 'English']
        report = task_func(students, subjects, seed=42)
        # Check if the number of rows matches the number of students
        self.assertEqual(len(report), len(students))
    def test_random_seed_reproducibility(self):
        students = ['Alice', 'Bob']
        subjects = ['Math', 'Physics']
        
        # If we run the function with the same seed, we should get the same results.
        report1 = task_func(students, subjects, seed=42)
        report2 = task_func(students, subjects, seed=42)
        pd.testing.assert_frame_equal(report1, report2)
    def test_without_seed(self):
        students = ['Alice', 'Bob']
        subjects = ['Math', 'Physics']
        
        # When run without a seed, there should be variability in results.
        report1 = task_func(students, subjects)  # No seed here
        report2 = task_func(students, subjects)  # No seed here
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(report1, report2)
