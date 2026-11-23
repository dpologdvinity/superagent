from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np

class TestCases(unittest.TestCase):

    def test_case_num_samples(self):
        """num_samples not an integer"""
        self.assertRaises(Exception, task_func, 'test')

    def test_case_1(self):
        demographics = task_func(10, rng_seed=1)
        self.assertEqual(len(demographics), 10)
        self.assertTrue(set(demographics['Country'].unique()).issubset(['Russia', 'China', 'USA', 'India', 'Brazil']))
        self.assertTrue(all((18 <= age <= 59 for age in demographics['Age'])))
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0, 1]))

    def test_case_2(self):
        demographics = task_func(5, countries=['Canada', 'Australia'], rng_seed=1)
        self.assertEqual(len(demographics), 5)
        self.assertTrue(set(demographics['Country'].unique()).issubset(['Canada', 'Australia']))
        self.assertTrue(all((18 <= age <= 59 for age in demographics['Age'])))
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0, 1]))
