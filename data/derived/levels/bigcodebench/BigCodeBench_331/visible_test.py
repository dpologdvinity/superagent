from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch
import random

class TestCases(unittest.TestCase):

    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_into_empty_list(self, mock_randint):
        random.seed(0)
        result = task_func(15, 0, 5, 60)
        self.assertEqual(result, ([], [15]))

    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_into_existing_list(self, mock_randint):
        random.seed(0)
        result = task_func(15, 5, 10, 60)
        self.assertEqual(result, ([12, 23, 34, 45, 56], [12, 15, 23, 34, 45, 56]))

    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_at_beginning(self, mock_randint):
        random.seed(0)
        result = task_func(4, 4, 10, 60)
        self.assertEqual(result, ([12, 23, 34, 45], [4, 12, 23, 34, 45]))
