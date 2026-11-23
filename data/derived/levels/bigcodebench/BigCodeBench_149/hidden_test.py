from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func(['hello'])
        expected = pd.DataFrame({'Element': ['hello'], 'Count': [5]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_2(self):
        result = task_func(['a', 'bc', 'def'])
        expected = pd.DataFrame({'Element': ['a', 'bc', 'def'], 'Count': [1, 2, 3]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_3(self):
        result = task_func(['zzz', 'zzz'])
        expected = pd.DataFrame({'Element': ['zzz', 'zzz'], 'Count': [3, 3]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_4(self):
        result = task_func(['hello world', 'open ai'])
        expected = pd.DataFrame({'Element': ['hello world', 'open ai'], 'Count': [11, 7]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_5(self):
        result = task_func(['hello', 'world'], include_index=True)
        expected = pd.DataFrame({'Index': np.array([0, 1], dtype='int64'), 'Element': ['hello', 'world'], 'Count': [5, 5]})
        pd.testing.assert_frame_equal(result, expected)
