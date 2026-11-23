from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        country_dict = {'John': 'USA', 'Alice': 'UK', 'Bob': 'China'}
        result = task_func(country_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.index), ['USA', 'UK', 'China'])
        self.assertTrue(result['GDP'].apply(lambda x: 1000000000 <= x <= 100000000000).all())
    def test_case_2(self):
        country_dict = {'Charlie': 'Japan', 'David': 'Australia'}
        result = task_func(country_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.index), ['Japan', 'Australia'])
        self.assertTrue(result['GDP'].apply(lambda x: 1000000000 <= x <= 100000000000).all())
    def test_case_3(self):
        country_dict = {'Eve': 'USA', 'Frank': 'UK', 'Grace': 'China', 'Hannah': 'Japan', 'Ian': 'Australia'}
        result = task_func(country_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.index), ['USA', 'UK', 'China', 'Japan', 'Australia'])
        self.assertTrue(result['GDP'].apply(lambda x: 1000000000 <= x <= 100000000000).all())
    def test_case_4(self):
        country_dict = {'Jack': 'USA'}
        result = task_func(country_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.index), ['USA'])
        self.assertTrue(result['GDP'].apply(lambda x: 1000000000 <= x <= 100000000000).all())
    def test_case_5(self):
        country_dict = {}
        result = task_func(country_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.index), [])
        self.assertTrue(result.empty)
