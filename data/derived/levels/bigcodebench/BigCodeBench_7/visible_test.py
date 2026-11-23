from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import os
import unittest
import csv

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.join(os.getcwd(), 'test_data')
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def test_case_1(self):
        self.create_csv('sales1.csv', [['product', 'quantity'], ['Product B', '200'], ['Product A', '100']])
        result = task_func(os.path.join(self.test_dir, 'sales1.csv'))
        self.assertEqual(result, 'Product B')

    def test_case_2(self):
        self.create_csv('sales2.csv', [['product', 'quantity'], ['Product Z', '120'], ['Product Y', '80']])
        result = task_func(os.path.join(self.test_dir, 'sales2.csv'))
        self.assertEqual(result, 'Product Z')

    def test_case_3(self):
        self.create_csv('sales3.csv', [['product', 'quantity'], ['Product M', '500'], ['Product N', '400']])
        result = task_func(os.path.join(self.test_dir, 'sales3.csv'))
        self.assertEqual(result, 'Product M')

    def create_csv(self, filename, rows):
        path = os.path.join(self.test_dir, filename)
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
