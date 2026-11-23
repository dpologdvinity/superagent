from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_1(self):
        # Testing basic functionality
        input_data = [10, 20, 30, 40, 50]
        expected_output = np.array([0. , 0.25, 0.5 , 0.75, 1. ])
        np.testing.assert_array_almost_equal(task_func(input_data), expected_output, decimal=2)
    def test_2(self):
        # Testing with negative values
        input_data = [-50, -40, -30, -20, -10]
        expected_output = np.array([0. , 0.25, 0.5 , 0.75, 1. ])
        np.testing.assert_array_almost_equal(task_func(input_data), expected_output, decimal=2)
    def test_3(self):
        # Testing with mixed negative and positive values
        input_data = [-50, -25, 0, 25, 50]
        expected_output = np.array([0. , 0.25, 0.5 , 0.75, 1. ])
        np.testing.assert_array_almost_equal(task_func(input_data), expected_output, decimal=2)
    def test_4(self):
        # Testing with single value
        input_data = [100]
        expected_output = np.array([0.])
        np.testing.assert_array_almost_equal(task_func(input_data), expected_output, decimal=2)
    def test_5(self):
        # Testing with all zeros
        input_data = [0, 0, 0, 0, 0]
        expected_output = np.array([0., 0., 0., 0., 0.])
        np.testing.assert_array_almost_equal(task_func(input_data), expected_output, decimal=2)
