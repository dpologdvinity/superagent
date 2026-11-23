from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil

class TestCases(unittest.TestCase):

    def setUp(self):
        os.mkdir('test_1')
        with open('test_1/file1.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([['header1', 'header2'], ['row1_col1', 'row1_col2'], ['row2_col1', 'row2_col2']])
        os.mkdir('test_2')
        with open('test_2/file2.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([['name', 'age'], ['Alice', '30'], ['Bob', '40']])
        os.mkdir('test_5')
        with open('test_5/file3.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([['subject', 'marks'], ['Math', '90'], ['Science', '85']])

    def tearDown(self):
        shutil.rmtree('test_1')
        shutil.rmtree('test_2')
        shutil.rmtree('test_5')

    def test_case_1(self):
        data = task_func('test_1')
        self.assertIsInstance(data, dict)
        self.assertIn('file1', data)
        self.assertEqual(data['file1'], [['header1', 'header2'], ['row1_col1', 'row1_col2'], ['row2_col1', 'row2_col2']])

    def test_case_2(self):
        data = task_func('test_2', '.csv')
        self.assertIsInstance(data, dict)
        self.assertIn('file2', data)
        self.assertEqual(data['file2'], [['name', 'age'], ['Alice', '30'], ['Bob', '40']])

    def test_case_3(self):
        data = task_func('test_3', '.txt')
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 0)
