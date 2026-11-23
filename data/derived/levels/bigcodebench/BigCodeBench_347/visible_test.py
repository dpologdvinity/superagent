from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import re
from faker import Faker
PATTERN = '([a-fA-F\\d]{32})'

def generate_mock_dataframe(num_rows, include_hex=True):
    fake = Faker()
    data = []
    for _ in range(num_rows):
        if include_hex:
            sentence = fake.sentence() + ' ' + fake.hexify(text='^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', upper=False)
        else:
            sentence = fake.sentence()
        data.append(sentence)
    return pd.DataFrame({'text': data})

class TestCases(unittest.TestCase):

    def test_typical_use_case(self):
        df = generate_mock_dataframe(10, include_hex=True)
        result = task_func(df, 'text')
        self.assertIsInstance(result, pd.Series)
        for hex_pattern in result.index:
            self.assertRegex(hex_pattern, PATTERN)

    def test_default(self):
        df = pd.DataFrame({'text': ['6f96cfdfe5ccc627cadf24b41725caa4 gorilla', '6f96cfdfe5ccc627cadf24b41725caa4 banana', '1234567890abcdef1234567890abcdef apple']})
        result = task_func(df, 'text')
        self.assertIsInstance(result, pd.Series)
        for hex_pattern in result.index:
            self.assertRegex(hex_pattern, PATTERN)

    def test_no_matches(self):
        df = generate_mock_dataframe(10, include_hex=False)
        result = task_func(df, 'text')
        self.assertTrue(result.empty)
