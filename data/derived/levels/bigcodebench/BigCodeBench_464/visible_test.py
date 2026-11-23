from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from datetime import datetime
from decimal import Decimal
import pytz

class TestCases(unittest.TestCase):

    def test_datetime_serialization(self):
        """Ensure datetime objects are serialized to an ISO 8601 string."""
        obj = {'time': datetime(2023, 1, 1, 12, 0, tzinfo=pytz.utc)}
        result = task_func(obj)
        self.assertIn('2023-01-01T12:00:00+00:00', result)

    def test_decimal_serialization(self):
        """Verify Decimal objects are serialized to their string representation."""
        obj = {'price': Decimal('99.99')}
        result = task_func(obj)
        self.assertIn('99.99', result)

    def test_combined_serialization(self):
        """Test serialization of a complex object containing both datetime and Decimal."""
        obj = {'time': datetime(2023, 1, 1, 12, 0, tzinfo=pytz.utc), 'price': Decimal('99.99')}
        result = task_func(obj)
        self.assertIn('2023-01-01T12:00:00+00:00', result)
        self.assertIn('99.99', result)
