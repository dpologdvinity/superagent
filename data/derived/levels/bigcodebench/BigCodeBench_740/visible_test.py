from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def generate_random_dict(size=26, min_val=1, max_val=100):
    """Generate a random dictionary with letters as keys and random integers as values."""
    letters = random.sample(LETTERS, size)
    return {letter: random.randint(min_val, max_val) for letter in letters}

class TestCases(unittest.TestCase):

    def test_basic(self):
        test_dict = generate_random_dict()
        result = task_func(test_dict)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertTrue(all((isinstance(letter, str) for letter in result)))

    def test_few_letters(self):
        test_dict = {'a': 10, 'b': 20}
        result = task_func(test_dict)
        self.assertEqual(result, ['b', 'a'])

    def test_empty_dict(self):
        test_dict = {}
        result = task_func(test_dict)
        self.assertEqual(result, [])
