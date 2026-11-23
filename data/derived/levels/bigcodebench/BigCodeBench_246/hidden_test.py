from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing basic functionality with 3 waves
        sine_waves, fft_data, ax = task_func(3)
        self.assertEqual(len(sine_waves), 3)  # Should return 3 waves
        self.assertTrue(isinstance(sine_waves[0], np.ndarray))  # Each wave should be a numpy array
        # Testing if the FFT data is a numpy array
        self.assertIsInstance(fft_data, np.ndarray)
        # Testing if the axes object is returned
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        # Testing with 5 waves
        sine_waves, fft_data, ax = task_func(5)
        self.assertEqual(len(sine_waves), 5)
        self.assertTrue(isinstance(sine_waves[4], np.ndarray))
        # Test the axis limits of the histogram
        self.assertAlmostEqual(ax.get_xlim()[1], 331.2, places=1)
        # Test the axis bins
        self.assertEqual(len(ax.patches), 10)
    def test_case_3(self):
        # Testing with 1 wave
        sine_waves, fft_data, ax = task_func(1, seed=5)
        self.assertEqual(len(sine_waves), 1)
        self.assertTrue(isinstance(sine_waves[0], np.ndarray))
        # Test the FFT data
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (629,))
        # test the maximum value of the FFT data
        self.assertAlmostEqual(np.max(np.abs(fft_data)), 314.3, places=1)
    def test_case_4(self):
        # Testing edge case with 0 waves
        sine_waves, fft_data, ax = task_func(0)
        self.assertEqual(len(sine_waves), 0)
        self.assertEqual(fft_data.shape, (0,))
        self.assertIsNone(ax)
    def test_case_5(self):
        # Testing with negative number, should return empty list
        sine_waves, fft_data, ax = task_func(-5)
        self.assertEqual(len(sine_waves), 0)
        self.assertEqual(fft_data.shape, (0,))
        self.assertIsNone(ax)
