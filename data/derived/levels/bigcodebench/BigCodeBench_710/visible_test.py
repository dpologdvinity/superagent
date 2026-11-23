from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import numpy as np

class TestCases(unittest.TestCase):

    def test_case_1(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        df = pd.DataFrame(data, columns=['a', 'b', 'c'])
        df.to_csv('data.csv', index=False)
        df = task_func('data.csv')
        self.assertEqual(df.shape, (3, 3))
        self.assertAlmostEqual(df['a'].min(), 0)
        self.assertAlmostEqual(df['a'].max(), 1)
        self.assertAlmostEqual(df['b'].min(), 0)
        self.assertAlmostEqual(df['b'].max(), 1)
        self.assertAlmostEqual(df['c'].min(), 0)
        self.assertAlmostEqual(df['c'].max(), 1)
        os.remove('data.csv')

    def test_case_2(self):
        data = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        df = pd.DataFrame(data, columns=['a', 'b', 'c'])
        df.to_csv('data.csv', index=False)
        df = task_func('data.csv')
        self.assertEqual(df.shape, (3, 3))
        self.assertAlmostEqual(df['a'].min(), 0)
        self.assertAlmostEqual(df['a'].max(), 0)
        self.assertAlmostEqual(df['b'].min(), 0)
        self.assertAlmostEqual(df['b'].max(), 0)
        self.assertAlmostEqual(df['c'].min(), 0)
        self.assertAlmostEqual(df['c'].max(), 0)
        os.remove('data.csv')

    def test_case_3(self):
        data = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        df = pd.DataFrame(data, columns=['a', 'b', 'c'])
        df.to_csv('data.csv', index=False)
        df = task_func('data.csv')
        self.assertEqual(df.shape, (3, 3))
        self.assertAlmostEqual(df['a'].min(), 0)
        self.assertAlmostEqual(df['a'].max(), 0)
        self.assertAlmostEqual(df['b'].min(), 0)
        self.assertAlmostEqual(df['b'].max(), 0)
        self.assertAlmostEqual(df['c'].min(), 0)
        self.assertAlmostEqual(df['c'].max(), 0)
        os.remove('data.csv')
