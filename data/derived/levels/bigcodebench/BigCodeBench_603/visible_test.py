from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import re

class TestCases(unittest.TestCase):

    def normalize_whitespace(self, string):
        """Normalize the whitespace in the string to a single space."""
        return re.sub('\\s+', ' ', string).strip()

    def test_basic_concatenation(self):
        """Test basic functionality of concatenating two matrices."""
        matrix1 = np.array([[1, 2], [3, 4]])
        matrix2 = np.array([[5, 6], [7, 8]])
        expected_output = ' 1  2  5  6\n 3  4  7  8'
        result = task_func(matrix1, matrix2)
        self.assertEqual(self.normalize_whitespace(result), self.normalize_whitespace(expected_output))

    def test_different_length_matrices(self):
        """Test concatenation of matrices with different numbers of rows."""
        matrix1 = np.array([[1, 2], [3, 4], [5, 6]])
        matrix2 = np.array([[7, 8]])
        with self.assertRaises(ValueError):
            task_func(matrix1, matrix2)

    def test_mismatched_dimensions(self):
        """Test concatenation with mismatched dimensions."""
        matrix1 = np.array([[1, 2]])
        matrix2 = np.array([[3], [4]])
        with self.assertRaises(ValueError):
            task_func(matrix1, matrix2)
