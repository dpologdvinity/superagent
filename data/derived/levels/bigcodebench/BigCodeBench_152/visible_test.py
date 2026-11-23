from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import random

class TestCases(unittest.TestCase):

    def setUp(self):
        random.seed(0)
        self.patcher = patch('random.randint', side_effect=[i % 100 for i in range(800)])
        self.mock_randint = self.patcher.start()
        self.grades_df = task_func()
        self.patcher.stop()

    def test_dataframe_columns(self):
        expected_columns = ['Name'] + COURSES + ['Average Grade']
        self.assertListEqual(list(self.grades_df.columns), expected_columns, 'DataFrame should have specific columns')

    def test_grade_range(self):
        course_columns = self.grades_df.columns[1:-1]
        for course in course_columns:
            self.assertTrue(self.grades_df[course].between(0, 100).all(), f'All grades in {course} should be between 0 and 100')

    def test_average_grade_calculation(self):
        course_columns = self.grades_df.columns[1:-1]
        calculated_avg = self.grades_df[course_columns].mean(axis=1)
        np.testing.assert_array_almost_equal(self.grades_df['Average Grade'], calculated_avg, decimal=1, err_msg='Average grades should be correctly calculated')
