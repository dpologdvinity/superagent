from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a dictionary."""
        result = task_func({'array': np.array([1, 2, 3])})
        self.assertIsInstance(result, dict)
    def test_normalized_array_presence(self):
        """Test that 'normalized_array' key is present in the returned dictionary."""
        result = task_func({'array': np.array([1, 2, 3])})
        self.assertIn('normalized_array', result)
    def test_normalized_array_values(self):
        """Test that the normalized array contains correct values."""
        input_array = np.array([10, 20, 30])
        expected_normalized = np.array([0., 0.5, 1.])
        result = task_func({'array': input_array})
        np.testing.assert_array_almost_equal(result['normalized_array'], expected_normalized)
    def test_single_value_array(self):
        """Test the function with a single value array."""
        result = task_func({'array': np.array([42])})
        self.assertEqual(result['normalized_array'][0], 0)  # Single value should be normalized to 0
    def test_inplace_modification(self):
        """Test that the function modifies the input dictionary in place."""
        input_dict = {'array': np.array([1, 2, 3])}
        result = task_func(input_dict)
        self.assertIs(result, input_dict)
        self.assertIn('normalized_array', input_dict)
    def test_negative_values_normalization(self):
        """Test normalization on an array with negative values."""
        input_array = np.array([-10, 0, 10])
        expected_normalized = np.array([0., 0.5, 1.])
        result = task_func({'array': input_array})
        np.testing.assert_array_almost_equal(result['normalized_array'], expected_normalized)
    def test_key_error_raise(self):
        """Test that a KeyError is raised if 'array' key is missing."""
        with self.assertRaises(KeyError):
            task_func({})
    def test_type_error_raise(self):
        """Test that a TypeError is raised if value is not a numpy array."""
        with self.assertRaises(TypeError):
            task_func({'array': [1, 2, 3]})
    @patch('sklearn.preprocessing.MinMaxScaler.fit_transform')
    def test_mock_minmaxscaler(self, mock_fit_transform):
        """Test the function with a mock of MinMaxScaler's fit_transform method."""
        input_array = np.array([1, 2, 3])
        mock_fit_transform.return_value = input_array.reshape(-1, 1)
        task_func({'array': input_array})
        mock_fit_transform.assert_called_once()
