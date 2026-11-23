from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = task_func({'key': 'value'})
        self.assertIn('key', result)
        self.assertIn('a', result)
        self.assertIn('timestamp', result)
        self.assertNotEqual(result['a'], '1')
        self.assertEqual(result['key'], '8691a011016e0fba3c2b0b8a26e4c9c722975f1defe42f580ab55a9c97dfccf8')
        self.assertEqual(result['a'], '373f3d39a5d5075dfb4503ebe44f70eed8a48e1a32be02d182b2a26695c6f694')
        self.assertIsInstance(result['timestamp'], float)

    def test_case_2(self):
        result = task_func({})
        self.assertIn('a', result)
        self.assertIn('timestamp', result)

    def test_case_3(self):
        result = task_func({'first': '1', 'second': '2'})
        self.assertIn('first', result)
        self.assertIn('second', result)
        self.assertIn('a', result)
        self.assertIn('timestamp', result)
        self.assertNotEqual(result['first'], '1')
        self.assertNotEqual(result['second'], '2')
