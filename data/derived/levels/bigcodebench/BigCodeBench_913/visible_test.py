from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_empty_list(self):
        expected = {'mode': np.array([], dtype='object').tolist(), 'count': np.array([], dtype=int).tolist(), 'fft': np.array([]).tolist()}
        result = task_func([], repetitions=1)
        self.assertEqual({'mode': result['mode'].tolist(), 'count': result['count'].tolist(), 'fft': result['fft'].tolist()}, expected)

    def test_single_mode(self):
        result = task_func([1, 2, 2, 3], repetitions=1)
        np.testing.assert_array_equal(result['mode'], np.array([2]))
        np.testing.assert_array_equal(result['count'], np.array([2]))
        np.testing.assert_array_equal(result['fft'], np.array([8.0 - 0j, -1.0 + 1j, -2.0 - 0j, -1.0 - 1j]))

    def test_multiple_modes_repeated(self):
        result = task_func(['00', '01'], repetitions=3)
        np.testing.assert_array_equal(result['mode'], np.array(['00', '01']))
        np.testing.assert_array_equal(result['count'], np.array([3, 3]))
        np.testing.assert_array_equal(result['fft'], np.array([1.0 - 0j, -1.0 - 0j]))
