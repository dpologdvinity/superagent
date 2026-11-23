from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from collections import Counter
HAND_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']

class TestCases(unittest.TestCase):

    def setUp(self) -> None:
        random.seed(42)

    def test_poker_hand_length(self):
        """Test if the poker hand has 5 cards."""
        hand, rank_counts = task_func()
        self.assertEqual(len(hand), 5, 'The poker hand should contain 5 cards.')

    def test_card_format(self):
        """Test if each card in the hand is formatted correctly."""
        hand, rank_counts = task_func()
        for card in hand:
            self.assertIn(len(card), [2, 3], 'Each card should be a string of length 2 or 3.')
            self.assertIn(card[:-1], HAND_RANKS, 'The rank of each card should be valid.')
            self.assertIn(card[-1], SUITS, 'The suit of each card should be valid.')

    def test_rank_counts_type(self):
        """Test if rank_counts is of type Counter."""
        hand, rank_counts = task_func()
        self.assertIsInstance(rank_counts, Counter, 'rank_counts should be a Counter dictionary.')
