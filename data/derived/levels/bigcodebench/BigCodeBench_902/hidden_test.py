from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(task_func([]), {'x': Counter(), 'y': Counter(), 'z': Counter()})
    def test_all_keys_present(self):
        data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 1, 'y': 3, 'z': 2}]
        expected = {'x': Counter({1: 2}), 'y': Counter({2: 1, 3: 1}), 'z': Counter({3: 1, 2: 1})}
        self.assertEqual(task_func(data), expected)
    def test_missing_keys(self):
        data = [{'x': 1}, {'y': 2}, {'z': 3}]
        expected = {'x': Counter({1: 1}), 'y': Counter({2: 1}), 'z': Counter({3: 1})}
        self.assertEqual(task_func(data), expected)
    def test_duplicate_values(self):
        data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 1, 'y': 2, 'z': 3}, {'x': 1, 'y': 2}]
        expected = {'x': Counter({1: 3}), 'y': Counter({2: 3}), 'z': Counter({3: 2})}
        self.assertEqual(task_func(data), expected)
    def test_mixed_data_types(self):
        data = [{'x': 1, 'y': 'a', 'z': 3.5}, {'x': '1', 'y': 'a', 'z': 3.5}]
        expected = {'x': Counter({1: 1, '1': 1}), 'y': Counter({'a': 2}), 'z': Counter({3.5: 2})}
        self.assertEqual(task_func(data), expected)
