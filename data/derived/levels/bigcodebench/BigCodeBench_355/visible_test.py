from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.signal import get_window

class TestCases(unittest.TestCase):

    def setUp(self):
        """Set up common constants for the tests."""
        self.amplitude = 1
        self.frequency = 5
        self.time = np.linspace(0, 1, 500, endpoint=False)

    def test_return_types(self):
        """Test that the function returns a numpy array, a matplotlib figure, and axes objects."""
        wave, fig, ax = task_func(self.amplitude, self.frequency, self.time)
        self.assertIsInstance(wave, np.ndarray)
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(ax, plt.Axes)

    def test_array_length(self):
        """Test the length of the returned array matches the length of the time array."""
        wave, _, _ = task_func(self.amplitude, self.frequency, self.time)
        self.assertEqual(len(wave), len(self.time))

    def test_wave_properties(self):
        """Test that the wave properties conform to expected cosine and sine functions with Hann window applied."""
        wave, _, _ = task_func(self.amplitude, self.frequency, self.time)
        window = get_window('hann', self.time.size)
        expected_wave = self.amplitude * np.exp(1j * 2 * math.pi * self.frequency * self.time) * window
        np.testing.assert_array_almost_equal(wave, expected_wave)
