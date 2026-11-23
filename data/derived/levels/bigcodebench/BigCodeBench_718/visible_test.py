from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import re
import numpy as np
from scipy.stats import ttest_rel

class TestCases(unittest.TestCase):

    def test_1(self):
        t_stat, p_val = task_func('Hello, world!', 'Hi, universe!')
        self.assertTrue(isinstance(t_stat, float))
        self.assertTrue(isinstance(p_val, float))

    def test_2(self):
        t_stat, p_val = task_func('Short text.', 'This is a slightly longer text.')
        self.assertTrue(isinstance(t_stat, float))
        self.assertTrue(isinstance(p_val, float))

    def test_3(self):
        t_stat, p_val = task_func('A, B, C, D, E.', 'F, G, H, I, J.')
        self.assertTrue(isinstance(t_stat, float))
        self.assertTrue(isinstance(p_val, float))
