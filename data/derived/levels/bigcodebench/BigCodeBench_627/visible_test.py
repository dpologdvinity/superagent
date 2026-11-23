from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        products = ['Apples']
        sales_data = task_func(products)
        expected_columns = ['Product'] + [f'Month {i + 1}' for i in range(12)] + ['Average Sales']
        self.assertEqual(list(sales_data.columns), expected_columns)
        avg_sales = sales_data['Average Sales'].iloc[0]
        self.assertAlmostEqual(avg_sales, sales_data.iloc[0, 1:13].mean(), places=2)
        self.assertTrue((sales_data.iloc[0, 1:13] >= 100).all() and (sales_data.iloc[0, 1:13] <= 500).all())

    def test_case_2(self):
        products = ['Apples', 'Bananas', 'Grapes']
        sales_data = task_func(products)
        self.assertEqual(len(sales_data), 3)

    def test_case_3(self):
        products = []
        sales_data = task_func(products)
        self.assertEqual(len(sales_data), 0)
