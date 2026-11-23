from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        # Example df to test for error handling
        self.df = pd.DataFrame(
            {"A": ["blue car red", "green apple yellow"], "B": [3, 4]}
        )
    def test_case_1(self):
        # Test case where no words match the pattern
        df = pd.DataFrame({"Text": ["apple orange", "blue red"], "Number": [1, 2]})
        pattern = r"\b(?:banana|green)\b"
        expected = df.copy()
        result = task_func(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_2(self):
        # Test case where all words in a column match the pattern
        df = pd.DataFrame({"Text": ["apple banana", "banana apple"], "Number": [1, 2]})
        pattern = r"\b(?:apple|banana)\b"
        expected = pd.DataFrame(
            {"Text": ["banana apple", "apple banana"], "Number": [1, 2]}
        )
        result = task_func(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_3(self):
        # Test case with a mix of matching and non-matching words
        df = pd.DataFrame(
            {"Text": ["apple orange banana", "blue apple green"], "Number": [1, 2]}
        )
        pattern = r"\b(?:apple|banana)\b"
        expected = pd.DataFrame(
            {"Text": ["banana orange apple", "blue apple green"], "Number": [1, 2]}
        )
        result = task_func(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_4(self):
        # Test case where the column contains an empty string
        df = pd.DataFrame({"Text": ["", "apple banana"], "Number": [1, 2]})
        pattern = r"\b(?:apple|banana)\b"
        expected = pd.DataFrame({"Text": ["", "banana apple"], "Number": [1, 2]})
        result = task_func(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_5(self):
        # Test case where the pattern is an empty string (matches nothing)
        df = pd.DataFrame({"Text": ["apple orange", "banana apple"], "Number": [1, 2]})
        pattern = ""
        expected = df.copy()
        result = task_func(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_6(self):
        # Test the function with a column name that does not exist in the DataFrame
        with self.assertRaises(KeyError):
            task_func(self.df, "NonexistentColumn", r"\b(?:car|apple|yellow)\b")
    def test_case_7(self):
        # Test the function with a non-string column name
        with self.assertRaises(KeyError):
            task_func(self.df, 123, r"\b(?:car|apple|yellow)\b")
    def test_case_8(self):
        # Test the function with an invalid regular expression pattern
        with self.assertRaises(re.error):
            task_func(self.df, "A", r"\b(?:car|apple|yellow")
