from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np

class TestCases(unittest.TestCase):

    def setUp(self):
        """ Set up for each test, fixing the random seed for reproducibility. """
        np.random.seed(0)

    def test_samples_length(self):
        """ Test if the number of generated samples is correct. """
        samples, _ = task_func(0, 1, 1000)
        self.assertEqual(len(samples), 1000)

    def test_samples_type(self):
        """ Test the type of the samples. """
        samples, _ = task_func(0, 1, 1000)
        self.assertIsInstance(samples, np.ndarray)

    def test_mean_approximation(self):
        """ Test if the mean of the samples is approximately equal to the specified mean. """
        samples, _ = task_func(0, 1, 1000)
        self.assertAlmostEqual(np.mean(samples), 0, places=1)
