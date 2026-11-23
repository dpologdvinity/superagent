from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        vegetable_dict = {'John': 'Carrot', 'Alice': 'Potato', 'Bob': 'Tomato'}
        result = task_func(vegetable_dict)
        self.assertIn('Carrot', result.index)
        self.assertIn('Potato', result.index)
        self.assertIn('Tomato', result.index)
        self.assertTrue(all(result['Percentage'] <= 100))
        self.assertTrue(all(result['Percentage'] >= 0))

    def test_case_2(self):
        vegetable_dict = {'Charlie': 'Cabbage', 'David': 'Spinach'}
        result = task_func(vegetable_dict)
        self.assertIn('Cabbage', result.index)
        self.assertIn('Spinach', result.index)
        self.assertTrue(all(result['Percentage'] <= 100))
        self.assertTrue(all(result['Percentage'] >= 0))

    def test_case_3(self):
        vegetable_dict = {}
        result = task_func(vegetable_dict)
        self.assertTrue(all(result['Percentage'] <= 100))
        self.assertTrue(all(result['Percentage'] >= 0))
