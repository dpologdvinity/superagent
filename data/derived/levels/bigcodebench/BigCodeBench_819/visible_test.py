from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import time

class TestCases(unittest.TestCase):

    def test_case_1(self):
        start_time = time.time()
        messages, total_delay = task_func(3, 0.2, 0.3, 12)
        elapsed_time = time.time() - start_time
        self.assertEqual(messages, ['0.25 seconds have passed', '0.27 seconds have passed', '0.27 seconds have passed'])
        self.assertAlmostEqual(elapsed_time, total_delay, delta=0.1)

    def test_case_2(self):
        start_time = time.time()
        result, total_delay = task_func(1, 0.5, 2.5, seed=42)
        elapsed_time = time.time() - start_time
        self.assertEqual(result, ['1.78 seconds have passed'])
        self.assertAlmostEqual(elapsed_time, total_delay, delta=0.1)

    def test_case_3(self):
        start_time = time.time()
        result, total_delay = task_func(seed=123)
        elapsed_time = time.time() - start_time
        self.assertEqual(result, ['1.05 seconds have passed', '1.09 seconds have passed', '1.41 seconds have passed', '1.11 seconds have passed', '1.90 seconds have passed'])
        self.assertAlmostEqual(elapsed_time, total_delay, delta=0.1)
