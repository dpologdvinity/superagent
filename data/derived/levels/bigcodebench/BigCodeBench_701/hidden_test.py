from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]], columns = ['x', 'y', 'z'])
        r_squared = task_func(df, 'z')
        self.assertEqual(r_squared, 1.0)
        
    def test_case_2(self):
        df = pd.DataFrame([[-1, 1, 2], [3, 4, 5], [6, 7, 8]], columns = ['x', 'y', 'z'])
        r_squared = task_func(df, 'z')
        self.assertEqual(r_squared, 1.0)
    
    def test_case_3(self):
        df = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]], columns = ['x', 'y', 'z'])
        r_squared = task_func(df, 'z')
        self.assertEqual(r_squared, 1.0)
    def test_case_4(self):
        df = pd.DataFrame([[0, 0, 9], [1, 1, 35], [2, 2, 78]], columns = ['x', 'y', 'z'])
        r_squared = task_func(df, 'z')
        self.assertFalse(r_squared == 1.0)
    def test_case_5(self):
        df = pd.DataFrame([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]], columns = ['x', 'y', 'z', 'w'])
        r_squared = task_func(df, 'w')
        self.assertEqual(r_squared, 1.0)
