from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_1(self):
        result = task_func([[1,2,3],[4,5,6]])
        expected = 2.5
        self.assertAlmostEqual(result, expected, places=2)
    def test_2(self):
        result = task_func([[1,1,1],[2,2,2]])
        expected = 1.0
        self.assertAlmostEqual(result, expected, places=2)
    def test_3(self):
        result = task_func([[1,5,3]])
        expected = 2.0
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_4(self):
        result = task_func([[1],[2],[3],[4],[5]])
        expected = 2.0
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_5(self):
        result = task_func([[1,-2,3],[-4,5,6]])
        expected = 5.75
        self.assertAlmostEqual(result, expected, places=2)
