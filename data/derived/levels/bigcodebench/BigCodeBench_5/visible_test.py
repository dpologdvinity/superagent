from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import math
import random

class TestCases(unittest.TestCase):

    def setUp(self):
        self.LETTERS = [chr(i) for i in range(97, 123)]
        random.seed(42)

    def test_default_letters(self):
        sd_dict = task_func()
        self.assertEqual(set(self.LETTERS), set(sd_dict.keys()))
        for val in sd_dict.values():
            self.assertGreaterEqual(val, 0)

    def test_custom_letters(self):
        custom_letters = ['x', 'y', 'z']
        sd_dict = task_func(custom_letters)
        self.assertEqual(set(custom_letters), set(sd_dict.keys()))
        for val in sd_dict.values():
            self.assertGreaterEqual(val, 0)

    @patch('random.randint')
    def test_uniform_values(self, mocked_randint):
        mocked_randint.side_effect = [3, 50, 50, 50, 3, 50, 50, 50]
        letters = ['a', 'b']
        sd_dict = task_func(letters)
        self.assertTrue(all((math.isclose(val, 0, abs_tol=1e-05) for val in sd_dict.values())))
