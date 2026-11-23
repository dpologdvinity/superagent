from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import numpy as np

class TestCases(unittest.TestCase):

    def test_return_type(self):
        """ Test that the function returns a numpy array. """
        result = task_func([1, 2, 3])
        self.assertIsInstance(result, np.ndarray)

    @patch('random.randint', return_value=50)
    def test_array_size(self, mock_randint):
        """ Test that the returned array has the correct size. """
        input_list = [1, 2, 3]
        expected_size = sum(input_list) + 50
        result = task_func(input_list)
        self.assertEqual(len(result), expected_size)

    @patch('random.randint', return_value=50)
    def test_list_modification(self, mock_randint):
        """ Test that the input list is modified correctly with a mocked random value. """
        input_list = [1, 2, 3]
        task_func(input_list)
        self.assertIn(50, input_list)
