from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
import doctest
import tempfile
from collections import Counter

class TestCases(unittest.TestCase):
    base_tmp_dir = tempfile.mkdtemp()
    test_data_dir = f'{base_tmp_dir}/test'

    def setUp(self):
        self.csv_file_path = 'data.csv'
        if not os.path.exists(self.test_data_dir):
            os.makedirs(self.test_data_dir)
        test_files = {'test1.csv': ['a', 'b', '(abc)', 'a', 'a', '(def)', 'b', '(ghi)', 'a', 'c', '(abc)'], 'test2.csv': ['x', 'y', '(xyz)', 'x', '(uvw)', 'z', 'y', '(rst)', '(xyz)'], 'test3.csv': ['1', '2', '(345)', '(678)', '2', '3', '(901)', '4', '(234)'], 'test4.csv': ['@', '#', '($%^)', '&', '*', '(*)_+', '@', '(#&)'], 'test5.csv': ['apple', 'banana', '(cherry)', 'date', '(fig)', 'grape', '(kiwi)', 'lemon', '(mango)']}
        self.file_paths = {}
        for file_name, data in test_files.items():
            file_path = os.path.join(self.test_data_dir, file_name)
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for item in data:
                    writer.writerow([item])
            self.file_paths[file_name] = file_path

    def tearDown(self):
        shutil.rmtree(self.test_data_dir)

    def test_case_1(self):
        result = task_func(self.file_paths['test1.csv'])
        expected = {'a': 4, ' ': 3, 'b': 2, ' (': 4, 'abc': 2, ') ': 3, 'def': 1, 'ghi': 1, 'c': 1, ')': 1}
        self.assertEqual(result, expected, f'Expected {expected} but got {result}')

    def test_case_2(self):
        result = task_func(self.file_paths['test2.csv'])
        expected = {'x': 2, ' ': 2, 'y': 2, ' (': 3, 'xyz': 2, ') ': 2, 'uvw': 1, 'z': 1, 'rst': 1, ') (': 1, ')': 1}
        self.assertEqual(result, expected, f'Expected {expected} but got {result}')

    def test_case_3(self):
        result = task_func(self.file_paths['test3.csv'])
        expected = {'1': 1, ' ': 2, '2': 2, ' (': 3, '345': 1, ') (': 1, '678': 1, ') ': 2, '3': 1, '901': 1, '4': 1, '234': 1, ')': 1}
        self.assertEqual(result, expected, f'Expected {expected} but got {result}')
