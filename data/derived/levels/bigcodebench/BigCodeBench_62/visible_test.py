from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    def test_case_1(self):
        random.seed(42)
        result = [{'from_user': 0}, {'from_user': 0}, {'from_user': 1}]
        with patch('matplotlib.pyplot.show') as mocked_show:
            task_func(result)
            mocked_show.assert_called_once()

    def test_case_2(self):
        random.seed(42)
        result = []
        with patch('matplotlib.pyplot.show') as mocked_show:
            task_func(result)
            mocked_show.assert_called_once()

    def test_case_3(self):
        random.seed(42)
        result = [{'hello': 0}, {'world': 1}]
        with patch('matplotlib.pyplot.show') as mocked_show:
            task_func(result)
            mocked_show.assert_called_once()
