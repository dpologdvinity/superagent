from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        sine_waves, fft_data, ax = task_func(3)
        self.assertEqual(len(sine_waves), 3)
        self.assertTrue(isinstance(sine_waves[0], np.ndarray))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertIsInstance(ax, plt.Axes)

    def test_case_2(self):
        sine_waves, fft_data, ax = task_func(5)
        self.assertEqual(len(sine_waves), 5)
        self.assertTrue(isinstance(sine_waves[4], np.ndarray))
        self.assertAlmostEqual(ax.get_xlim()[1], 331.2, places=1)
        self.assertEqual(len(ax.patches), 10)

    def test_case_3(self):
        sine_waves, fft_data, ax = task_func(1, seed=5)
        self.assertEqual(len(sine_waves), 1)
        self.assertTrue(isinstance(sine_waves[0], np.ndarray))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (629,))
        self.assertAlmostEqual(np.max(np.abs(fft_data)), 314.3, places=1)
