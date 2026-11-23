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
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [81 for i in range(rows)],
                'D': [900 for i in range(rows)] 
            }
        )
        self.assertRaises(Exception, task_func, data)
    def test_column_number(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [81 for i in range(rows)],
                'C': [900 for i in range(rows)] 
            }
        )
        self.assertRaises(Exception, task_func, data, ['A'])
        self.assertRaises(Exception, task_func, data, ['A', 'B', 'C', 'D'])
    def test_no_data_after_filer(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [20 for i in range(rows)],
                'C': [901 for i in range(rows)] 
            }
        )
        self.assertRaises(Exception, task_func, data)
    def test_medium_dataframe(self):
        # Test with a medium-sized dataframe (50 rows)
        fake = faker.Faker()
        fake.seed_instance(12)
        rows = 50
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [fake.random_int(0, 100) for i in range(rows)],
                'C': [fake.random_int(899, 901) for i in range(rows)] 
            }
        )        
        p_value = task_func(data)
        self.assertAlmostEqual(p_value, 0.23, places=1)
    def test_large_dataframe(self):
        # Test with a large dataframe (1000 rows)
        fake = faker.Faker()
        fake.seed_instance(21)
        rows = 1000
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [fake.random_int(0, 100) for i in range(rows)],
                'C': [fake.random_int(800, 950) for i in range(rows)] 
            }
        )        
        p_value = task_func(data)
        self.assertAlmostEqual(p_value, 0.22, places=1)
    def test_very_large_dataframe(self):
        data = pd.DataFrame(
            {
                'A': ['a', 'a', 'a', 'a', 'a'],
                'B': [70, 70, 70, 70, 70],
                'C': [900, 900, 900, 900, 900] 
            }
        )
        p_value = task_func(data)
        self.assertAlmostEqual(p_value, 1.0, places=1)
    def test_huge_dataframe(self):
        # different column names
        fake = faker.Faker()
        fake.seed_instance(21)
        rows = 1000
        data = pd.DataFrame(
            {
                'test': [fake.name() for i in range(rows)],
                'five': [fake.random_int(21, 150) for i in range(rows)],
                '1': [fake.random_int(821, 950) for i in range(rows)] 
            }
        )        
        p_value = task_func(data, columns=['test', 'five', '1'])
        self.assertAlmostEqual(p_value, 0.22, places=1)
    def test_diff_filter(self):
        # different filter values
        fake = faker.Faker()
        fake.seed_instance(21)
        rows = 1000
        data = pd.DataFrame(
            {
                'test': [fake.name() for i in range(rows)],
                'five': [fake.random_int(21, 150) for i in range(rows)],
                '1': [fake.random_int(19, 21) for i in range(rows)] 
            }
        )        
        p_value = task_func(data, columns=['test', 'five', '1'], larger=100, equal=20)
        self.assertAlmostEqual(p_value, 0.35, places=1)
