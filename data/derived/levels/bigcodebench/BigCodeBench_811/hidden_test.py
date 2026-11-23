from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        dictionary = [['Apple', 'Banana', 'Orange', 'Apple', 'Banana'] for _ in range(5)]
        positions, df = task_func(dictionary, 'Apple')
        self.assertListEqual(sorted(positions), sorted([(0, 0), (0, 3), (1, 0), (1, 3), (2, 0), (2, 3), (3, 0), (3, 3), (4, 0), (4, 3)]))
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
    def test_case_2(self):
        dictionary = [['Orange', 'Banana', 'Apple', 'Apple', 'Banana'] for _ in range(5)]
        positions, df = task_func(dictionary, 'Apple')
        self.assertListEqual(sorted(positions), sorted([(0, 2), (0, 3), (1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3), (4, 2), (4, 3)]))
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
    def test_case_3(self):
        dictionary = [['Apple', 'Banana', 'Apple', 'Orange', 'Banana'] for _ in range(5)]
        positions, df = task_func(dictionary, 'Orange')
        self.assertListEqual(positions, [(i, 3) for i in range(5)])
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
    def test_case_4(self):
        dictionary = [['Banana', 'Banana', 'Banana', 'Banana', 'Banana'] for _ in range(5)]
        positions, df = task_func(dictionary, 'Apple')
        self.assertListEqual(positions, [])
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
    def test_case_5(self):
        dictionary = [['Apple', 'Apple', 'Apple', 'Apple', 'Apple'] for _ in range(5)]
        positions, df = task_func(dictionary, 'Apple')
        self.assertListEqual(positions, [(i, j) for i in range(5) for j in range(5)])
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
    def test_case_6(self):
        dictionary = [['Apple', 'Banana', 'Orange', 'Apple', 'Banana'] for _ in range(5)]
        sample_size = 3
        seed_value = 42
        positions_sampled, df = task_func(dictionary, 'Apple', sample_size=sample_size, random_seed=seed_value)
        self.assertEqual(len(positions_sampled), sample_size)
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
    def test_case_7(self):
        dictionary = [['Apple', 'Banana', 'Orange', 'Apple', 'Banana'] for _ in range(10)]
        sample_size = 5
        seed_value = 42
        positions_sampled_1, df = task_func(dictionary, 'Apple', sample_size=sample_size, random_seed=seed_value)
        positions_sampled_2, df = task_func(dictionary, 'Apple', sample_size=sample_size, random_seed=seed_value)
        self.assertListEqual(positions_sampled_1, positions_sampled_2)
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
