from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os, shutil
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_folder = tempfile.mkdtemp()

    def test_case_1(self):
        result = task_func(['a', 'b', 'a', 'c', 'a'], 'a', self.temp_folder)
        self.assertEqual(result, 3)
        with open(self.temp_folder + '/task_func.log') as log:
            self.assertTrue("INFO:Function called with list: ['a', 'b', 'a', 'c', 'a'] and element: a" in log.readline())
            self.assertTrue("INFO:Frequency of 'a' is 3" in log.readline())

    def test_case_2(self):
        result = task_func(['x', 'y', 'z'], 'y', self.temp_folder)
        self.assertEqual(result, 1)
        with open(self.temp_folder + '/task_func.log') as log:
            self.assertTrue("INFO:Function called with list: ['x', 'y', 'z'] and element: y" in log.readline())
            self.assertTrue("INFO:Frequency of 'y' is 1" in log.readline())

    def test_case_3(self):
        result = task_func(['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'], 'r', self.temp_folder)
        self.assertEqual(result, 1)
        with open(self.temp_folder + '/task_func.log') as log:
            self.assertTrue("INFO:Function called with list: ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'] and element: r" in log.readline())
            self.assertTrue("INFO:Frequency of 'r' is 1" in log.readline())
