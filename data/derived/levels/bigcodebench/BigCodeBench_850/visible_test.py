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
        self.assertIsInstance(report, pd.DataFrame)
        expected_columns = ['Student'] + subjects + ['Average Grade']
        self.assertEqual(list(report.columns), expected_columns)

    def test_average_grade_calculation(self):
        students = ['Alice']
        subjects = ['Math', 'Physics']
        report = task_func(students, subjects, seed=42)
        alice_grades = report.iloc[0, 1:-1]
        self.assertEqual(report.at[0, 'Average Grade'], alice_grades.mean())

    def test_varying_input_sizes(self):
        students = ['Alice', 'Bob', 'Charlie']
        subjects = ['Math', 'Physics', 'Biology', 'English']
        report = task_func(students, subjects, seed=42)
        self.assertEqual(len(report), len(students))
