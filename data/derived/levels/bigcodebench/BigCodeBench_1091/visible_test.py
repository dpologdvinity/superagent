from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import ast
import shutil

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'testdir_task_func'
        os.makedirs(self.test_dir, exist_ok=True)
        self.sample_directory = 'testdir_task_func/sample_directory'
        os.makedirs(self.sample_directory, exist_ok=True)
        f = open(self.sample_directory + '/1.txt', 'w')
        f.write("{'key1': 'value1'}")
        f.close()
        f = open(self.sample_directory + '/2.txt', 'w')
        f.write("{'key2': 'value2', 'key3': 'value3'}")
        f.close()
        f = open(self.sample_directory + '/3.txt', 'w')
        f.write("{'key4': 'value4'}")
        f.close()
        f = open(self.sample_directory + '/4.txt', 'w')
        f.write("{'key5': 'value5', 'key6': 'value6', 'key7': 'value7'}")
        f.close()
        f = open(self.sample_directory + '/5.txt', 'w')
        f.write("{'key8': 'value8'}")
        f.close()
        self.empty_directory = 'testdir_task_func/empty_directory'
        os.makedirs(self.empty_directory, exist_ok=True)
        self.multi_line_directory = 'testdir_task_func/multi_line_directory'
        os.makedirs(self.multi_line_directory, exist_ok=True)
        f = open(self.multi_line_directory + '/1.txt', 'w')
        f.write("{'key1': 'value1'}\n{'key2': 'value2'}")
        f.close()
        self.mixed_directory = 'testdir_task_func/mixed_directory'
        os.makedirs(self.mixed_directory, exist_ok=True)
        f = open(self.mixed_directory + '/1.txt', 'w')
        f.write('invalid')
        f.close()
        self.invalid_directory = 'testdir_task_func/invalid_directory'
        os.makedirs(self.invalid_directory, exist_ok=True)
        f = open(self.invalid_directory + '/1.txt', 'w')
        f.write('invalid')
        f.close()
        f = open(self.invalid_directory + '/2.txt', 'w')
        f.write("{'key1': 'value1'}")
        f.close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_case_1(self):
        result = task_func(self.sample_directory)
        expected_result = [{'key1': 'value1'}, {'key2': 'value2', 'key3': 'value3'}, {'key4': 'value4'}, {'key5': 'value5', 'key6': 'value6', 'key7': 'value7'}, {'key8': 'value8'}]
        for i in expected_result:
            self.assertTrue(i in result)

    def test_case_2(self):
        result = task_func(self.empty_directory)
        self.assertEqual(result, [])

    def test_case_3(self):
        with self.assertRaises(ValueError):
            task_func(self.invalid_directory)
