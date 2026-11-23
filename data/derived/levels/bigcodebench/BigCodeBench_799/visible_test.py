from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from faker import Faker
import pandas as pd
fake = Faker()

def generate_fake_data(num_rows=5, num_columns=5):
    """Generate fake data for test cases"""
    fake.seed_instance(12)
    data = []
    for _ in range(num_rows):
        row = [fake.random_int() for _ in range(num_columns)]
        data.append(row)
    return data

class TestCases(unittest.TestCase):

    def test_rng(self):
        data = generate_fake_data(5, 3)
        result1, _ = task_func(data, random_seed=12)
        result2, _ = task_func(data, random_seed=12)
        result3, _ = task_func(data, random_seed=1)
        pd.testing.assert_frame_equal(result1, result2)
        try:
            pd.testing.assert_frame_equal(result1, result3)
        except AssertionError:
            pass
        else:
            raise AssertionError

    def test_case_1(self):
        data = generate_fake_data(5, 3)
        result, df_list = task_func(data, random_seed=123)
        expected = pd.DataFrame({'b': {0: 7775, 1: 3729, 3: 177, 4: 5730}, 'c': {0: 4407, 1: 9145, 3: 6139, 4: 2336}, 'k': {0: 8669, 1: 27, 3: 7905, 4: 6252}})
        pd.testing.assert_frame_equal(result, expected)
        self.assertEqual(len(df_list), 5)
        self.assertEqual(len(df_list[0]), 3)

    def test_case_2(self):
        data = generate_fake_data(10, 5)
        result, df_list = task_func(data, random_seed=42)
        expected = pd.DataFrame({'q': {0: 995, 1: 5120, 2: 7775, 5: 7540, 6: 8413}, 'a': {0: 8338, 1: 9144, 2: 4407, 5: 9854, 6: 5521}, 'h': {0: 3657, 1: 2679, 2: 8669, 5: 3729, 6: 6629}, 'f': {0: 1490, 1: 841, 2: 5730, 5: 9145, 6: 1431}, 't': {0: 6943, 1: 9095, 2: 2336, 5: 27, 6: 304}})
        pd.testing.assert_frame_equal(result, expected)
        self.assertEqual(len(df_list), 5)
        self.assertEqual(len(df_list[0]), 3)
