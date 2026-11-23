from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_rng(self):
        output1 = task_func(2, 123)
        output2 = task_func(2, 123)
        self.assertCountEqual(output1, output2)
    
    def test_case_1(self):
        output = task_func(2, 123)
        self.assertEqual(len(output), 10)
        self.assertTrue(all(len(word) == 2 for word in output))
        self.assertTrue(all(word.islower() for word in output))
        expected = ['tq', 'ob', 'os', 'mk', 'du', 'ar', 'wx', 'ec', 'et', 'vx']
        self.assertCountEqual(output, expected)
        
    def test_case_2(self):
        output = task_func(3, 456)
        self.assertEqual(len(output), 10)
        self.assertTrue(all(len(word) == 3 for word in output))
        self.assertTrue(all(word.islower() for word in output))
        expected = ['axp', 'xtb', 'pwx', 'rxv', 'soa', 'rkf', 'cdp', 'igv', 'ruh', 'vmz']
        self.assertCountEqual(output, expected)
        
    def test_case_3(self):
        output = task_func(2, 789, alphabets=['x', 'y', 'z'])
        self.assertEqual(len(output), 10)
        self.assertTrue(all(len(word) == 2 for word in output))
        self.assertTrue(all(letter in ['x', 'y', 'z'] for word in output for letter in word))
        expected = ['yx', 'xz', 'xy', 'yx', 'yy', 'zz', 'yy', 'xy', 'zz', 'xx']
        self.assertCountEqual(output, expected)
    def test_case_4(self):
        output = task_func(1, 100)
        self.assertEqual(len(output), 10)
        self.assertTrue(all(len(word) == 1 for word in output))
        self.assertTrue(all(word.islower() for word in output))
        expected = ['i', 'y', 'd', 'h', 'x', 'p', 'q', 'k', 'u', 'c']
        self.assertCountEqual(output, expected)
        
    def test_case_5(self):
        output = task_func(4, 200, alphabets=['a', 'b'])
        self.assertEqual(len(output), 10)
        self.assertTrue(all(len(word) == 4 for word in output))
        self.assertTrue(all(letter in ['a', 'b'] for word in output for letter in word))
        expected = ['baba', 'baab', 'aaaa', 'abaa', 'baba', 'abbb', 'bbaa', 'bbbb', 'baab', 'bbba']
        self.assertCountEqual(output, expected)
