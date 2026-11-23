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
        # Test with a list of two plot names
        output = task_func(["Plot 1", "Plot 2"], self.test_dir, seed=1)
        expected = ["Plot_1.png", "Plot_2.png"]
        self.assertEqual(output, expected)
        for file_name in expected:
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, file_name)))
    def test_case_2(self):
        # Test directory creation if not exists
        path = os.path.join(self.test_dir, "foo", "bar", "temp")
        self.assertFalse(os.path.exists(path))
        output = task_func(["Test A", "Test B", "Test C"], path, seed=2)
        expected = ["Test_A.png", "Test_B.png", "Test_C.png"]
        self.assertEqual(output, expected)
        for file_name in expected:
            self.assertTrue(os.path.exists(os.path.join(path, file_name)))
    def test_case_3(self):
        # Test with an empty list of plot names to ensure no files are created.
        output = task_func([], self.test_dir, seed=3)
        self.assertEqual(output, [])
        self.assertEqual(len(os.listdir(self.test_dir)), 0)
    def test_case_4(self):
        # Test with a list of plot names containing special characters.
        output = task_func(["Test@A", "Test#B", "Test&C"], self.test_dir, seed=4)
        expected = ["Test@A.png", "Test#B.png", "Test&C.png"]
        self.assertEqual(output, expected)
        for file_name in expected:
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, file_name)))
    def test_case_5(self):
        # Test with a single-element list of plot names, ensuring the function can handle minimal input.
        output = task_func(["Single Plot"], self.test_dir, seed=5)
        expected = ["Single_Plot.png"]
        self.assertEqual(output, expected)
        for file_name in expected:
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, file_name)))
    def test_case_6(self):
        # Test with name deduplication
        output = task_func(["Single Plot"] * 5, self.test_dir, seed=6)
        expected = ["Single_Plot.png"]
        self.assertEqual(output, expected)
        for file_name in expected:
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, file_name)))
