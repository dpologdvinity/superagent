from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import faker

class TestCases(unittest.TestCase):

    def test_column_not_in_df(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame({'A': [fake.name() for i in range(rows)], 'B': [81 for i in range(rows)], 'D': [900 for i in range(rows)]})
        self.assertRaises(Exception, task_func, data)

    def test_column_number(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame({'A': [fake.name() for i in range(rows)], 'B': [81 for i in range(rows)], 'C': [900 for i in range(rows)]})
        self.assertRaises(Exception, task_func, data, ['A'])
        self.assertRaises(Exception, task_func, data, ['A', 'B', 'C', 'D'])

    def test_no_data_after_filer(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame({'A': [fake.name() for i in range(rows)], 'B': [20 for i in range(rows)], 'C': [901 for i in range(rows)]})
        self.assertRaises(Exception, task_func, data)
