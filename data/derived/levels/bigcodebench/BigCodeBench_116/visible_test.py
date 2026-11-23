from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):

    def test_return_type(self):
        """ Test that the function returns a numpy array. """
        result = task_func(0, 1, 1000)
        self.assertIsInstance(result, np.ndarray)

    def test_sample_size(self):
        """ Test that the returned array has the correct size. """
        result = task_func(0, 1, 1000)
        self.assertEqual(len(result), 1000)

    def test_normal_distribution_properties(self):
        """ Test if the generated samples have the correct mean and standard deviation. """
        mu, sigma = (0, 1)
        result = task_func(mu, sigma, 1000000)
        self.assertAlmostEqual(np.mean(result), mu, places=1)
        self.assertAlmostEqual(np.std(result), sigma, places=1)
