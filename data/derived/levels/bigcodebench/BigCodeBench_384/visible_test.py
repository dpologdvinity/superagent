from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_dict = {'John': 'Cat', 'Alice': 'Dog', 'Bob': 'Elephant'}
        expected_output = {'Cat': ['John'], 'Dog': ['Alice'], 'Elephant': ['Bob']}
        reversed_dict, animal_counter = task_func(input_dict)
        self.assertEqual(reversed_dict, expected_output)
        self.assertEqual(set(animal_counter.keys()), set(ANIMALS))

    def test_case_2(self):
        _, animal_counter = task_func({})
        for animal in ANIMALS:
            self.assertIn(animal, animal_counter)
            self.assertTrue(1 <= animal_counter[animal] <= 10)

    def test_case_3(self):
        _, animal_counter = task_func({}, 17, 42)
        target = {'Rabbit': 14, 'Elephant': 9, 'Lion': 8, 'Tiger': 8, 'Bear': 5, 'Cat': 4, 'Giraffe': 4, 'Horse': 3, 'Snake': 2, 'Dog': 1, 'Zebra': 1}
        self.assertEqual(animal_counter, target)
