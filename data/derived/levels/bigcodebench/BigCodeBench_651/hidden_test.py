from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test case with default example data
        df = {
            'Column1': ['0', 'a', '332', '33'],
            'Column2': ['1', 'bb', '33', '22'],
            'Column3': ['2', 'ccc', '2', '332']
        }
        counts, ax = task_func(df, '332')
        self.assertEqual(counts['Column1'], 1)
        self.assertEqual(counts['Column2'], 0)
        self.assertEqual(counts['Column3'], 1)
    def test_case_2(self):
        # Test case with no occurrences of the target value
        df = {
            'Column1': ['0', 'a', '331', '33'],
            'Column2': ['1', 'bb', '33', '22'],
            'Column3': ['2', 'ccc', '2', '331']
        }
        counts, ax = task_func(df, '332')
        self.assertEqual(counts['Column1'], 0)
        self.assertEqual(counts['Column2'], 0)
        self.assertEqual(counts['Column3'], 0)
    def test_case_3(self):
        # Test case with multiple occurrences of the target value in a single column
        df = {
            'Column1': ['332', 'a', '332', '33'],
            'Column2': ['1', '332', '332', '22'],
            'Column3': ['2', '332', '2', '332']
        }
        counts, ax = task_func(df, '332')
        self.assertEqual(counts['Column1'], 2)
        self.assertEqual(counts['Column2'], 2)
        self.assertEqual(counts['Column3'], 2)
    def test_case_4(self):
        # Test case with an empty DataFrame
        df = pd.DataFrame()
        counts, ax = task_func(df, '332')
        self.assertEqual(len(counts), 0)
    def test_case_5(self):
        # Test case with different data types in the DataFrame
        df = {
            'Column1': [0, 'a', 332, '33'],
            'Column2': [1.0, 'bb', 33.0, 22.2],
            'Column3': [2, 'ccc', 2, 332]
        }
        counts, ax = task_func(df, '332')
        self.assertEqual(counts['Column1'], 1)
        self.assertEqual(counts['Column2'], 0)
        self.assertEqual(counts['Column3'], 1)
