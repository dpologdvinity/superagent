from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from faker import Faker
import math

class TestCases(unittest.TestCase):
    faker = Faker()

    def test_rng(self):
        pairs1 = task_func(random_seed=42)
        pairs2 = task_func(random_seed=42)
        for _ in range(10):
            self.assertEqual(next(pairs1), next(pairs2))

    def test_case_1(self):
        pairs = task_func(random_seed=1)
        self.assertIsInstance(pairs, type((x for x in range(1))))
        expected = [(18, 73, 7.416198487095663), (98, 9, 9.433981132056603), (33, 16, 4.123105625617661), (64, 98, 5.830951894845301), (58, 61, 1.7320508075688772), (84, 49, 5.916079783099616), (27, 13, 3.7416573867739413), (63, 4, 7.681145747868608), (50, 56, 2.449489742783178), (78, 98, 4.47213595499958)]
        for _ in range(10):
            x, y, diff = next(pairs)
            self.assertEqual(diff, math.sqrt(abs(x - y)))
            self.assertEqual((x, y, diff), expected[_])

    def test_case_2(self):
        pairs = task_func(50, 150, random_seed=12)
        self.assertIsInstance(pairs, type((x for x in range(1))))
        expected = [(110, 84, 5.0990195135927845), (134, 117, 4.123105625617661), (135, 94, 6.4031242374328485), (68, 98, 5.477225575051661), (51, 97, 6.782329983125268), (111, 85, 5.0990195135927845), (132, 108, 4.898979485566356), (138, 126, 3.4641016151377544), (79, 121, 6.48074069840786), (50, 134, 9.16515138991168)]
        for _ in range(10):
            x, y, diff = next(pairs)
            self.assertTrue(50 <= x <= 150)
            self.assertTrue(50 <= y <= 150)
            self.assertEqual(diff, math.sqrt(abs(x - y)))
            self.assertEqual((x, y, diff), expected[_])
