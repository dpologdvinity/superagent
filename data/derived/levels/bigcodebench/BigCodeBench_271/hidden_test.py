from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with a simple dictionary
        result = task_func({'key': 'value'})
        # The result should have 3 keys now: key, a, and timestamp
        self.assertIn('key', result)
        self.assertIn('a', result)
        self.assertIn('timestamp', result)
        # The value for 'a' should be hashed
        self.assertNotEqual(result['a'], '1')
        self.assertEqual(result['key'], '8691a011016e0fba3c2b0b8a26e4c9c722975f1defe42f580ab55a9c97dfccf8')
        self.assertEqual(result['a'], '373f3d39a5d5075dfb4503ebe44f70eed8a48e1a32be02d182b2a26695c6f694')
        self.assertIsInstance(result['timestamp'], float)
    def test_case_2(self):
        # Testing with an empty dictionary
        result = task_func({})
        # The result should have 2 keys now: a, and timestamp
        self.assertIn('a', result)
        self.assertIn('timestamp', result)
    def test_case_3(self):
        # Testing with a dictionary having multiple key-value pairs
        result = task_func({'first': '1', 'second': '2'})
        # The result should have 4 keys now: first, second, a, and timestamp
        self.assertIn('first', result)
        self.assertIn('second', result)
        self.assertIn('a', result)
        self.assertIn('timestamp', result)
        # The values should be hashed
        self.assertNotEqual(result['first'], '1')
        self.assertNotEqual(result['second'], '2')
    def test_case_4(self):
        # Testing with a dictionary having non-string values
        result = task_func({'number': 123, 'float': 45.67}, seed=11)
        # The result should have 4 keys now: number, float, a, and timestamp
        self.assertIn('number', result)
        self.assertIn('float', result)
        self.assertIn('a', result)
        self.assertIn('timestamp', result)
        # The values should be hashed
        self.assertNotEqual(result['number'], '123')
        self.assertNotEqual(result['float'], '45.67')
        self.assertEqual(result['number'], '99a44a377de81b704fcc13054924e260927064689112828e9385597a93d65f76')
        self.assertEqual(result['float'], '69e1ba5bed469d999e8d79b4ddbd5a96671502264c0bb0b005ded4e4d5057f16')
        self.assertEqual(result['a'], 'c2189c194ccc63dc89a683f1b0e9682a423681074b4a69832de82ed4eaaa2ac7')
        self.assertIsInstance(result['timestamp'], float)
    def test_case_5(self):
        # Testing with a dictionary having special characters in values
        result = task_func({'special': '!@#$%^'})
        # The result should have 3 keys now: special, a, and timestamp
        self.assertIn('special', result)
        self.assertIn('a', result)
        self.assertIn('timestamp', result)
        # The values should be hashed
        self.assertNotEqual(result['special'], '!@#$%^')
