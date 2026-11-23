from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import os

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_excel_file = 'dummy_test.xlsx'
        self.test_csv_file = 'dummy_test.csv'
        self.test_sheet_name = 'TestSheet'
        data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
        df = pd.DataFrame(data)
        df.to_excel(self.test_excel_file, sheet_name=self.test_sheet_name, index=False)

    def tearDown(self):
        os.remove(self.test_excel_file)
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)

    def test_normal_functionality(self):
        result = task_func(self.test_sheet_name, self.test_excel_file, self.test_csv_file)
        self.assertEqual(result, {'A': 60, 'B': 150})

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_sheet_name, 'nonexistent.xlsx', self.test_csv_file)

    def test_sheet_not_found(self):
        with self.assertRaises(ValueError):
            task_func('NonexistentSheet', self.test_excel_file, self.test_csv_file)
