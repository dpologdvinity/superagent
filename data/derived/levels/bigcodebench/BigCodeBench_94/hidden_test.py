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
    def test_std_dev_approximation(self):
        """ Test if the standard deviation of the samples is approximately equal to the specified standard deviation. """
        samples, _ = task_func(0, 1, 1000)
        self.assertAlmostEqual(np.std(samples), 1, places=1)
    def test_plot_title(self):
        """ Test if the plot title correctly reflects the mean and standard deviation. """
        _, fig = task_func(0, 1, 1000)
        self.assertIn("mean = 0.00,  std = 1.00", fig.axes[0].get_title())
    def test_histogram_bins(self):
        """ Test if the histogram displays the correct number of bins. """
        _, fig = task_func(0, 1, 1000)
        self.assertEqual(len(fig.axes[0].patches), 30)  # Check for 30 bins, as defined in the function
    def test_pdf_overlay(self):
        """ Test if the probability density function (PDF) is correctly overlayed on the histogram. """
        _, fig = task_func(0, 1, 1000)
        lines = fig.axes[0].get_lines()
        self.assertGreater(len(lines), 0)  # Ensure that at l
    def test_pdf_overlay_accuracy(self):
        """ Test if the PDF overlay accurately represents the normal distribution. """
        mean, std_dev, num_samples = 0, 1, 1000
        _, fig = task_func(mean, std_dev, num_samples)
        ax = fig.axes[0]
        line = ax.get_lines()[0]  # Assuming the first line is the PDF
        x, y = line.get_data()
        expected_y = norm.pdf(x, mean, std_dev)
        np.testing.assert_array_almost_equal(y, expected_y, decimal=2)
