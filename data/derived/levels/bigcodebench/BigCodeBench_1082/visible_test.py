from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):
    """Test cases for task_func"""

    def test_normal_operation(self):
        """
        Test normal operation with valid input.
        """
        data = {'Score_String': ['80.5', '85.7', '90.2'], 'Grade': ['B', 'B+', 'A-']}
        result = task_func(data)
        self.assertIsInstance(result, float)

    def test_empty_input(self):
        """
        Test the function with empty input.
        """
        data = {'Score_String': [], 'Grade': []}
        result = task_func(data)
        self.assertTrue(pd.isna(result))

    def test_invalid_score_format(self):
        """
        Test the function with invalid score format.
        """
        data = {'Score_String': ['eighty', '85.7', '90.2'], 'Grade': ['B', 'B+', 'A-']}
        with self.assertRaises(ValueError):
            task_func(data)
