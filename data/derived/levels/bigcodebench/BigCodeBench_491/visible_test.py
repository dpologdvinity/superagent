from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta

class TestCases(unittest.TestCase):

    def _check_sales_data(self, sales_data, expected_days):
        """Utility function to validate sales data."""
        self.assertIsInstance(sales_data, dict)
        self.assertEqual(set(sales_data.keys()), set(['Electronics', 'Clothing', 'Home', 'Books', 'Sports']))
        for category, sales in sales_data.items():
            self.assertEqual(len(sales), expected_days)
            for sale in sales:
                self.assertGreaterEqual(sale, 10)
                self.assertLessEqual(sale, 50)

    def test_case_1(self):
        sales_data, ax = task_func(1609459200000, seed=1)
        self.assertIsInstance(sales_data, dict)
        self.assertIsInstance(ax, plt.Axes)
        self._check_sales_data(sales_data, (datetime.now() - datetime.utcfromtimestamp(1609459200000 / 1000.0)).days)
        self.assertEqual(ax.get_ylabel(), 'Sales')

    def test_case_2(self):
        current_epoch = int(datetime.now().timestamp() * 1000)
        with self.assertRaises(ValueError):
            task_func(current_epoch, seed=2)

    def test_case_3(self):
        t = 1609459200000
        sales_data1, _ = task_func(t, seed=42)
        sales_data2, _ = task_func(t, seed=42)
        sales_data3, _ = task_func(t, seed=3)
        self.assertEqual(sales_data1, sales_data2)
        self.assertNotEqual(sales_data1, sales_data3)

    def tearDown(self):
        plt.close('all')
