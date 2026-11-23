from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    """Test cases for task_func"""

    def test_future_date_valid_booking_data(self):
        """
        Test task_func with a future date and valid booking data.
        """
        future_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        booking_data = {'Room1': 'Booked', 'Room2': 'Available'}
        report_df, _ = task_func(future_date, booking_data)
        self.assertIn('Room1', report_df['Room'].values)
        self.assertIn('Booked', report_df['Booking Status'].values)

    def test_past_date(self):
        """
        Test task_func with a past date to ensure it raises a ValueError.
        """
        past_date = '2020-01-01'
        booking_data = {'Room1': 'Booked'}
        with self.assertRaises(ValueError):
            task_func(past_date, booking_data)

    def test_invalid_date_format(self):
        """
        Test task_func with an invalid date format to check for ValueError.
        """
        invalid_date = '15-06-2023'
        booking_data = {'Room1': 'Booked'}
        with self.assertRaises(ValueError):
            task_func(invalid_date, booking_data)

    def tearDown(self):
        plt.clf()
