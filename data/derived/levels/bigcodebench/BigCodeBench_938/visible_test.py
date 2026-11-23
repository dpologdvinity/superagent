from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'text': ['hello', 'world', 'Special $#! characters   spaces 888323', 'Hello, World!', '', None]})

    def test_clean_text_and_calculate_length(self):
        result = task_func(self.df)
        expected_clean_text = ['hello', 'world', 'Specialcharactersspaces888323', 'HelloWorld', '', '']
        expected_text_length = [5, 5, 29, 10, 0, 0]
        pd.testing.assert_series_equal(result['clean_text'], pd.Series(expected_clean_text, name='clean_text'), check_names=False)
        pd.testing.assert_series_equal(result['text_length'], pd.Series(expected_text_length, name='text_length'), check_names=False)

    def test_with_special_characters(self):
        df = pd.DataFrame({'text': ['@@@hello***', '%%%world$$$']})
        result = task_func(df)
        self.assertEqual(result['clean_text'].iloc[0], 'hello')
        self.assertEqual(result['clean_text'].iloc[1], 'world')
        self.assertEqual(result['text_length'].iloc[0], 5)
        self.assertEqual(result['text_length'].iloc[1], 5)

    def test_with_numeric_strings(self):
        df = pd.DataFrame({'text': ['123', '4567']})
        result = task_func(df)
        self.assertEqual(result['clean_text'].iloc[0], '123')
        self.assertEqual(result['clean_text'].iloc[1], '4567')
        self.assertEqual(result['text_length'].iloc[0], 3)
        self.assertEqual(result['text_length'].iloc[1], 4)
