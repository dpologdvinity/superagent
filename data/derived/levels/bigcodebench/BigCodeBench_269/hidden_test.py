from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data_dict = {'key1': 2, 'key2': 4}
        modified_data, stats, plot = task_func(data_dict)
        self.assertEqual(modified_data, {'key1': 2, 'key2': 4, 'a': 1})
        self.assertEqual(stats['mean'], 2.33)
        self.assertEqual(stats['median'], 2.0)
        self.assertEqual(stats['mode'], 1)
        self.assertEqual(plot.get_title(), "Histogram of Normalized Values")
        self.assertEqual(plot.get_xlabel(), "Value")
        self.assertEqual(plot.get_ylabel(), "Frequency")
    def test_case_2(self):
        data_dict = {}
        modified_data, stats, plot = task_func(data_dict)
        self.assertEqual(modified_data, {'a': 1})
        self.assertEqual(stats['mean'], 1.0)
        self.assertEqual(stats['median'], 1.0)
        self.assertEqual(stats['mode'], 1)
        
    def test_case_3(self):
        data_dict = {'key1': 10, 'key2': 20, 'key3': 30}
        modified_data, stats, plot = task_func(data_dict)
        self.assertEqual(stats['mean'], 15.25)
        self.assertEqual(stats['median'], 15.0)
        self.assertEqual(stats['mode'], 1)
        
    def test_case_4(self):
        data_dict = {'key1': -5, 'key2': -10}
        modified_data, stats, plot = task_func(data_dict)
        self.assertEqual(stats['mean'], -4.67)
        self.assertEqual(stats['median'], -5.0)
        self.assertEqual(stats['mode'], -10)
        
    def test_case_5(self):
        data_dict = {'key1': 0, 'key2': 0, 'key3': 0, 'key4': 0}
        modified_data, stats, plot = task_func(data_dict)
        self.assertEqual(stats['mean'], 0.2)
        self.assertEqual(stats['median'], 0.0)
        self.assertEqual(stats['mode'], 0)
