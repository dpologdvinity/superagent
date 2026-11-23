from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_default_animals(self):
        report = task_func()
        self.assertEqual(len(report), 5)
        self.assertListEqual(list(report['Animal']), ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda'])
        df_list = report.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        with open('df_contents.txt', 'w') as file:
            file.write(str(df_list))
        expect = ['Lion,42.0,30.5,95,33.250563904992646', 'Elephant,44.4,41.5,12,34.1970758983864', 'Tiger,61.1,71.0,30,28.76264939118092', 'Giraffe,51.8,54.5,54,29.208902752414375', 'Panda,35.8,32.0,44,24.595934623429134']
        self.assertEqual(df_list, expect, 'DataFrame contents should match the expected output')

    def test_custom_animals(self):
        custom_animals = ['Dog', 'Cat']
        report = task_func(custom_animals)
        self.assertEqual(len(report), len(custom_animals))
        self.assertListEqual(list(report['Animal']), custom_animals)

    def test_statistics_columns(self):
        report = task_func()
        expected_columns = ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
        self.assertListEqual(list(report.columns), expected_columns)
