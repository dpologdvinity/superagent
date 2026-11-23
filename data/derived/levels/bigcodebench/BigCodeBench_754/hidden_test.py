from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_non_numeric(self):
        result = [{'from_user': 'a'}, {'from_user': 1}]
        self.assertRaises(Exception, task_func, result)
    def test_case_1(self):
        result = [{"hi": 7, "bye": 4, "from_user": 0}, {"from_user": 0}, {"from_user": 1}]
        summary = task_func(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertAlmostEqual(summary['mean'], 0.333333, places=5)
        self.assertEqual(summary['median'], 0.0)
        self.assertEqual(summary['min'], 0.0)
        self.assertEqual(summary['max'], 1.0)
        self.assertAlmostEqual(summary['std'], 0.471405, places=5)
    def test_case_2(self):
        result = [{"from_user": 1}, {"from_user": 2}, {"from_user": 3}]
        summary = task_func(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertEqual(summary['mean'], 2.0)
        self.assertEqual(summary['median'], 2.0)
        self.assertEqual(summary['min'], 1.0)
        self.assertEqual(summary['max'], 3.0)
        self.assertAlmostEqual(summary['std'], 0.816497, places=5)
    def test_case_3(self):
        result = [{"from_user": 5}]
        summary = task_func(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertEqual(summary['mean'], 5.0)
        self.assertEqual(summary['median'], 5.0)
        self.assertEqual(summary['min'], 5.0)
        self.assertEqual(summary['max'], 5.0)
        self.assertEqual(summary['std'], 0.0)
    def test_case_4(self):
        result = [{"hello": 2}, {"world": 3}]
        summary = task_func(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertTrue(np.isnan(summary['mean']))
        self.assertTrue(np.isnan(summary['median']))
        self.assertTrue(np.isnan(summary['min']))
        self.assertTrue(np.isnan(summary['max']))
        self.assertTrue(np.isnan(summary['std']))
    def test_case_5(self):
        'empty list'
        result = []
        summary = task_func(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertTrue(np.isnan(summary['mean']))
        self.assertTrue(np.isnan(summary['median']))
        self.assertTrue(np.isnan(summary['min']))
        self.assertTrue(np.isnan(summary['max']))
        self.assertTrue(np.isnan(summary['std']))
    
    
    def test_case_6(self):
        'float'
        result = [{"hi": 7, "bye": 4, "from_user": 0.3},
                  {"from_user": 0.1},
                  {"from_user": 15.6},
                  {"from_user": -2.3},
                  {"from_user": 12.12},
                  {"from_user": -25.234},
                  {"from_user": 124.2},
                  ]
        summary = task_func(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertAlmostEqual(summary['mean'], 17.826571, places=5)
        self.assertEqual(summary['median'], 0.3)
        self.assertEqual(summary['min'], -25.234)
        self.assertEqual(summary['max'], 124.2)
        self.assertAlmostEqual(summary['std'], 45.092813, places=5)
