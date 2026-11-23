from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import binascii

class TestCases(unittest.TestCase):

    def test_valid_signature(self):
        self.assertTrue(task_func('SGVsbG8gV29ybGQ=', 'c47c23299efca3c220f4c19a5f2e4ced14729322', 'my_secret_key'))

    def test_invalid_signature(self):
        self.assertFalse(task_func('SGVsbG8gV29ybGQ=', 'incorrect_signature', 'my_secret_key'))

    def test_empty_message(self):
        self.assertTrue(task_func('', '4b4f493acb45332879e4812a98473fc98209fee6', 'my_secret_key'))
