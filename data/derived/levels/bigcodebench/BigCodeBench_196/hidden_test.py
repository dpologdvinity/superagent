from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        _, data = task_func(1000)
        self.assertEqual(len(data), 1000)
    def test_case_2(self):
        with self.assertRaises(ValueError):
            _, data = task_func(1000, -3, 42)
        
    def test_case_3(self):
        _, data = task_func(20, 75, 77)
        self.assertEqual(data, [1, 4, 15, 19, 23, 25, 25, 26, 31, 31, 33, 36, 38, 42, 61, 64, 65, 65, 72, 72])
        self.assertTrue(all(1 <= num <= 75 for num in data))
    def test_case_4(self):
        ax, data = task_func(1000, 75)
        target = np.array([98, 103, 106, 73, 87, 92, 94, 84, 90, 95, 78])
        self.assertTrue((ax.containers[0].datavalues == target).all()) 
    def test_case_5(self):
        _, data1 = task_func(1000, seed=42)
        _, data2 = task_func(1000, seed=42)
        self.assertEqual(data1, data2)
