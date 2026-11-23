from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_data = ['lamp, bag, mirror', 'table, chair, bag, lamp']
        result = task_func(input_data, seed=0)
        self.assertTrue(all((item in input_data for item in result['Original String'])))
        self.assertNotEqual(result['Original String'].tolist(), result['Modified String'].tolist())

    def test_case_2(self):
        input_data = ['lamp, bag, mirror']
        result = task_func(input_data, seed=0)
        self.assertTrue(all((item in input_data for item in result['Original String'])))
        self.assertNotEqual(result['Original String'].tolist(), result['Modified String'].tolist())

    def test_case_3(self):
        input_data = ['lamp, chair', 'table, mirror, bag', 'desk, bed']
        result = task_func(input_data, seed=0)
        self.assertTrue(all((item in input_data for item in result['Original String'])))
        self.assertNotEqual(result['Original String'].tolist(), result['Modified String'].tolist())
