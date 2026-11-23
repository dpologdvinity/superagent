from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_time_until_new_year(self):
        self.assertIsInstance(task_func('2023-12-31 23:59:59', 'UTC'), int)

    def test_start_of_year(self):
        self.assertIsInstance(task_func('2023-01-01 00:00:00', 'UTC'), int)

    def test_leap_year(self):
        self.assertIsInstance(task_func('2024-02-29 00:00:00', 'UTC'), int)
