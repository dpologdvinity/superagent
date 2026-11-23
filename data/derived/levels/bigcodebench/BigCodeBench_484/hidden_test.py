from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        df = task_func(0, 10000, 100, random_seed=42)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(
            list(df.columns),
            ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"],
        )
        self.assertTrue(
            (df["SensorStatus"].isin(["OK", "MAINTENANCE_REQUIRED", "ERROR"])).all()
        )
    def test_case_2(self):
        # Test custom columns
        columns = ["Time", "Sensor_A", "Sensor_B", "Sensor_C", "Status"]
        statuses = ["WORKING", "NEEDS_CHECK", "FAILED"]
        df = task_func(
            1500, 3000, 50, columns=columns, sensor_statuses=statuses, random_seed=42
        )
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(list(df.columns), columns)
        self.assertTrue((df["Status"].isin(statuses)).all())
    def test_case_3(self):
        # Test generated data integrity by comparing with expected results
        np.random.seed(42)
        ts = 0  # Using the starting timestamp for simplicity
        expected_sensor1 = math.sin(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        expected_sensor2 = math.cos(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        expected_sensor3 = math.tan(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        df = task_func(0, 100, 100, random_seed=42)
        self.assertAlmostEqual(df.iloc[0]["Sensor1"], expected_sensor1, places=5)
        self.assertAlmostEqual(df.iloc[0]["Sensor2"], expected_sensor2, places=5)
        self.assertAlmostEqual(df.iloc[0]["Sensor3"], expected_sensor3, places=5)
    def test_case_4(self):
        # Test handling invalid start times
        with self.assertRaises(ValueError):
            task_func(10000, 0, 100)
    def test_case_5(self):
        # Test handling incorrect end times
        with self.assertRaises(ValueError):
            task_func(1000, 900, 100)
    def test_case_6(self):
        # Test column handling
        columns = ["Time", "Value1", "Value2", "Value3", "MachineStatus"]
        df = task_func(0, 500, 100, columns=columns)
        self.assertEqual(list(df.columns), columns)
        # Too few/too many columns
        with self.assertRaises(ValueError):
            task_func(0, 500, 100, columns[:-1])
        with self.assertRaises(ValueError):
            task_func(0, 500, 100, columns + ["foo", "bar"])
    def test_case_7(self):
        # Test sensor status handling
        with self.assertRaises(ValueError):
            task_func(0, 500, 100, [])
        statuses = ["RUNNING", "SHUTDOWN", "ERROR"]
        df = task_func(0, 500, 100, sensor_statuses=statuses)
        self.assertTrue((df["SensorStatus"].isin(statuses)).all())
    def test_case_8(self):
        # Test random seed
        df1 = task_func(0, 500, 100, random_seed=42)
        df2 = task_func(0, 500, 100, random_seed=42)
        pd.testing.assert_frame_equal(df1, df2)
    def test_case_9(self):
        # Test invalid steps handling
        with self.assertRaises(ValueError):
            task_func(0, 1000, -100)  # Step is negative
        with self.assertRaises(ValueError):
            task_func(0, 1000, 0)  # Step is zero
