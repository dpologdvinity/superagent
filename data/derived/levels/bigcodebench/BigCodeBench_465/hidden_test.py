from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from datetime import datetime
from decimal import Decimal
import numpy as np
import pytz
class TestCases(unittest.TestCase):
    def test_datetime_serialization(self):
        """Test serialization of datetime objects."""
        obj = {'time': datetime(2023, 1, 1, 12, 0, tzinfo=pytz.utc)}
        result = task_func(obj)
        self.assertIn('2023-01-01T12:00:00+00:00', result)
    def test_decimal_serialization(self):
        """Test serialization of Decimal objects."""
        obj = {'price': Decimal('99.99')}
        result = task_func(obj)
        self.assertIn('99.99', result)
    def test_numpy_array_serialization(self):
        """Test serialization of numpy arrays."""
        obj = {'data': np.array([1, 2, 3])}
        result = task_func(obj)
        self.assertIn('[1, 2, 3]', result)
    def test_combined_serialization(self):
        """Test combined serialization of datetime, numpy array, and Decimal."""
        obj = {'time': datetime(2023, 1, 1, 12, 0, tzinfo=pytz.utc), 'data': np.array([1, 2, 3]), 'price': Decimal('99.99')}
        result = task_func(obj)
        self.assertIn('2023-01-01T12:00:00+00:00', result)
        self.assertIn('[1, 2, 3]', result)
        self.assertIn('99.99', result)
    def test_simple_object_serialization(self):
        """Test serialization of simple objects (e.g., string, int)."""
        obj = {'name': 'Alice', 'age': 30}
        result = task_func(obj)
        self.assertEqual(result, '{"name": "Alice", "age": 30}')
    def test_unsupported_type_fallback(self):
        """Test that unsupported types fall back to the default encoder."""
        class UnsupportedType:
            pass
        obj = {'unsupported': UnsupportedType()}
        with self.assertRaises(TypeError):
            task_func(obj)
