from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import matplotlib.pyplot as plt
import shutil

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_images'

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_case_1(self):
        output = task_func(['Plot 1', 'Plot 2'], self.test_dir, seed=1)
        expected = ['Plot_1.png', 'Plot_2.png']
        self.assertEqual(output, expected)
        for file_name in expected:
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, file_name)))

    def test_case_2(self):
        path = os.path.join(self.test_dir, 'foo', 'bar', 'temp')
        self.assertFalse(os.path.exists(path))
        output = task_func(['Test A', 'Test B', 'Test C'], path, seed=2)
        expected = ['Test_A.png', 'Test_B.png', 'Test_C.png']
        self.assertEqual(output, expected)
        for file_name in expected:
            self.assertTrue(os.path.exists(os.path.join(path, file_name)))

    def test_case_3(self):
        output = task_func([], self.test_dir, seed=3)
        self.assertEqual(output, [])
        self.assertEqual(len(os.listdir(self.test_dir)), 0)
