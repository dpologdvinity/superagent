from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df = task_func(0, 10000, 100, random_seed=42)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(list(df.columns), ['Timestamp', 'Sensor1', 'Sensor2', 'Sensor3', 'SensorStatus'])
        self.assertTrue(df['SensorStatus'].isin(['OK', 'MAINTENANCE_REQUIRED', 'ERROR']).all())

    def test_case_2(self):
        columns = ['Time', 'Sensor_A', 'Sensor_B', 'Sensor_C', 'Status']
        statuses = ['WORKING', 'NEEDS_CHECK', 'FAILED']
        df = task_func(1500, 3000, 50, columns=columns, sensor_statuses=statuses, random_seed=42)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(list(df.columns), columns)
        self.assertTrue(df['Status'].isin(statuses).all())

    def test_case_3(self):
        np.random.seed(42)
        ts = 0
        expected_sensor1 = math.sin(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        expected_sensor2 = math.cos(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        expected_sensor3 = math.tan(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        df = task_func(0, 100, 100, random_seed=42)
        self.assertAlmostEqual(df.iloc[0]['Sensor1'], expected_sensor1, places=5)
        self.assertAlmostEqual(df.iloc[0]['Sensor2'], expected_sensor2, places=5)
        self.assertAlmostEqual(df.iloc[0]['Sensor3'], expected_sensor3, places=5)
