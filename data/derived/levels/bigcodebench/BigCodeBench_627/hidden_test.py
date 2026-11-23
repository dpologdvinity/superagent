from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a single product
        products = ["Apples"]
        sales_data = task_func(products)
        
        # Checking if returned DataFrame has the correct structure
        expected_columns = ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']
        self.assertEqual(list(sales_data.columns), expected_columns)
        
        # Checking the correctness of average sales
        avg_sales = sales_data['Average Sales'].iloc[0]
        self.assertAlmostEqual(avg_sales, sales_data.iloc[0, 1:13].mean(), places=2)
        
        # Checking if sales values are within the expected range
        self.assertTrue((sales_data.iloc[0, 1:13] >= 100).all() and (sales_data.iloc[0, 1:13] <= 500).all())
    def test_case_2(self):
        # Test with multiple products
        products = ["Apples", "Bananas", "Grapes"]
        sales_data = task_func(products)
        self.assertEqual(len(sales_data), 3)
    def test_case_3(self):
        # Test with no products
        products = []
        sales_data = task_func(products)
        self.assertEqual(len(sales_data), 0)
    def test_case_4(self):
        # Test with a long product name
        products = ["A" * 100]
        sales_data = task_func(products)
        self.assertEqual(sales_data['Product'].iloc[0], "A" * 100)
    def test_case_5(self):
        # Test with products having special characters
        products = ["@pples", "!Bananas", "#Grapes"]
        sales_data = task_func(products)
        self.assertTrue(all(item in sales_data['Product'].tolist() for item in products))
