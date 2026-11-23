from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        """test with normal input data"""
        input_data = [('traditional', -4), ('we', 7), ('because', 3), ('ability', 10), ('exactly', -7)]
        result = task_func(input_data)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('Value' in result.columns)
        self.assertAlmostEqual(result[result['Category'] == 'traditional']['Value'].item(), 0.176471, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'we']['Value'].item(), 0.823529, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'because']['Value'].item(), 0.588235, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'ability']['Value'].item(), 1.0, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'exactly']['Value'].item(), 0.0, places=6)

    def test_case_2(self):
        """test empty input"""
        input_data = []
        self.assertRaises(Exception, task_func, input_data)

    def test_case_3(self):
        """non numeric values"""
        input_data = [('fast', 'test'), ('ago', -8), ('player', 7), ('standard', 2), ('specific', 0)]
        self.assertRaises(Exception, task_func, input_data)
