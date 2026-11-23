from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random

class TestCases(unittest.TestCase):

    def test_case_1(self):
        d = {'EMP$$1': 10, 'MAN$$1': 5, 'EMP$$2': 8, 'HR$$1': 7}
        random.seed(0)
        emp_data = task_func(d)
        self.assertIn('EMP$$1', emp_data)
        self.assertIn('EMP$$2', emp_data)
        self.assertNotIn('MAN$$1', emp_data)
        self.assertNotIn('HR$$1', emp_data)
        self.assertEqual(len(emp_data['EMP$$1']), 10)
        self.assertEqual(len(emp_data['EMP$$2']), 8)

    def test_case_2(self):
        d = {'EMP$$A': 5, 'DEV$$A': 5}
        random.seed(0)
        emp_data = task_func(d)
        self.assertIn('EMP$$A', emp_data)
        self.assertNotIn('DEV$$A', emp_data)
        self.assertEqual(len(emp_data['EMP$$A']), 5)

    def test_case_3(self):
        d = {'MAN$$1': 5, 'HR$$1': 7}
        random.seed(0)
        emp_data = task_func(d)
        self.assertNotIn('MAN$$1', emp_data)
        self.assertNotIn('HR$$1', emp_data)
