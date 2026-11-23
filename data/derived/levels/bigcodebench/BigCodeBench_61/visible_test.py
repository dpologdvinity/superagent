from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import matplotlib

class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""

    def test_case_1(self):
        data = [{'key_1': 7, 'key_2': 4, 'from_user': 16}, {'key_1': 2, 'key_2': 4, 'from_user': 9}]
        square_roots, ax = task_func(data)
        self.assertEqual(ax.get_title(), PLOT_TITLE)
        self.assertEqual(ax.get_xlabel(), X_LABEL)
        self.assertEqual(ax.get_ylabel(), Y_LABEL)
        np.testing.assert_array_equal(square_roots, np.array([4.0, 3.0]))
        annotations = [child for child in ax.get_children() if isinstance(child, matplotlib.text.Annotation)]
        try:
            datetime.strptime(annotations[0].get_text(), TIME_FORMAT)
        except:
            raise ValueError(f'The datetime in annotation ({annotations[0]}) does not have the right format ({TIME_FORMAT}).')

    def test_case_2(self):
        data = [{'key_1': 7, 'key_2': 4}]
        square_roots, ax = task_func(data)
        self.assertEqual(len(square_roots), 0)

    def test_case_3(self):
        data = []
        square_roots, ax = task_func(data)
        self.assertEqual(len(square_roots), 0)
