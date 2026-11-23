from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class MockedSentimentIntensityAnalyzer:

    def polarity_scores(self, text):
        return {'compound': 0.5, 'neg': 0.25, 'neu': 0.25, 'pos': 0.5}

class TestCases(unittest.TestCase):

    def test_case_1(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = task_func('I love Python!', sia)
        expected = {'compound': 0.5, 'neg': 0.25, 'neu': 0.25, 'pos': 0.5}
        self.assertEqual(result, expected)

    def test_case_2(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = task_func('I hate rainy days.', sia)
        self.assertEqual(result['neg'], 0.25)

    def test_case_3(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = task_func('The weather is neutral today.', sia)
        self.assertEqual(result['neu'], 0.25)
