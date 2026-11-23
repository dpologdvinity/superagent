from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os 
class TestCases(unittest.TestCase):
    def test_average_similarity(self):
        s_list = ['apple', 'apples', 'ape', 'app', 'april']
        expected_length = len(s_list)
        result = task_func(s_list)
        expect = [0.7522727272727273, 0.6969696969696969, 0.6458333333333333, 0.6458333333333333, 0.5363636363636364]
        self.assertEqual(len(result), expected_length)
        self.assertTrue(all(isinstance(score, float) for score in result))
        self.assertAlmostEqual(result, expect,)
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            task_func([1, 2, 3])
    def test_empty_list(self):
        result = task_func([])
        self.assertEqual(result, [])
    def test_single_string(self):
        result = task_func(['apple'])
        self.assertTrue(np.isnan(result[0])) 
    def test_plot_saving(self):
        s_list = ['apple', 'apples', 'ape']
        plot_path = 'test_plot.png'
        task_func(s_list, plot_path)
        self.assertTrue(os.path.exists(plot_path))
        os.remove(plot_path)
