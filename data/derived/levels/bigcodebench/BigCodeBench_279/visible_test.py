from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import random

class TestCases(unittest.TestCase):

    def test_hand_size(self):
        """ Test if the hand contains exactly 5 cards. """
        random.seed(0)
        hand, _ = task_func()
        self.assertEqual(len(hand[0]), 5)

    def test_drawn_size(self):
        random.seed(0)
        hand, _ = task_func(2)
        self.assertEqual(len(hand[0]), 5)
        self.assertEqual(len(hand), 2)

    def test_counter(self):
        random.seed(0)
        hand, counter = task_func(1)
        self.assertEqual(len(hand[0]), 5)
        self.assertLessEqual(counter[hand[0][0]], 5)
        self.assertGreaterEqual(counter[hand[0][0]], 1)
