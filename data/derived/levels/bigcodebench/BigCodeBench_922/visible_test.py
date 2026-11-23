from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd

class TestCases(unittest.TestCase):

    def test_case_1(self):
        data = {'text': ['This is a sample sentence.', 'Another example here.']}
        expected_df = pd.DataFrame({'text': ['sample sentence', 'Another example']})
        result_df = task_func(data, 'text')
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_case_2(self):
        data = {'content': ['Stopwords should be removed.', 'Testing this function.']}
        expected_df = pd.DataFrame({'content': ['Stopwords removed', 'Testing function']})
        result_df = task_func(data, 'content')
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_case_3(self):
        data = {'sentence': ['Hello world!', 'Good morning.']}
        expected_df = pd.DataFrame({'sentence': ['Hello world', 'Good morning']})
        result_df = task_func(data, 'sentence')
        pd.testing.assert_frame_equal(result_df, expected_df)
