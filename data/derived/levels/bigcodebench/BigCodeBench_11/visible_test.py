from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch

class TestCases(unittest.TestCase):

    @patch('random.randint')
    def test_case_1(self, mock_randint):
        """Test with diverse values and the default range to ensure percentile calculation."""
        mock_randint.return_value = 50
        T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
        p25, p50, p75 = task_func(T1)
        self.assertEqual(p25, 50)
        self.assertEqual(p50, 50)
        self.assertEqual(p75, 50)

    @patch('random.randint')
    def test_case_2(self, mock_randint):
        """Check consistency when the total number of elements are small but repeated."""
        mock_randint.return_value = 30
        T1 = (('10',), ('10', '10', '10'))
        p25, p50, p75 = task_func(T1)
        self.assertEqual(p25, 30)
        self.assertEqual(p50, 30)
        self.assertEqual(p75, 30)

    @patch('random.randint')
    def test_case_3(self, mock_randint):
        """Ensure that percentile calculations are consistent for mixed low and medium values."""
        mock_randint.return_value = 75
        T1 = (('5', '5', '5', '5'), ('10', '15'), ('1', '2', '3', '4', '5'))
        p25, p50, p75 = task_func(T1)
        self.assertEqual(p25, 75)
        self.assertEqual(p50, 75)
        self.assertEqual(p75, 75)
