from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
class TestCases(unittest.TestCase):
    def test_high_accuracy(self):
        accuracy, warning_msg = task_func()
        self.assertGreaterEqual(accuracy, 0.8)
        self.assertIsNone(warning_msg)
    def test_low_accuracy_warning(self):
        accuracy, warning_msg = task_func()
        if accuracy < 0.9:
            self.assertEqual(warning_msg, "The accuracy of the SVM classification is below 0.9.")
    def test_accuracy_range(self):
        accuracy, _ = task_func()
        self.assertGreaterEqual(accuracy, 0)
        self.assertLessEqual(accuracy, 1)
    def test_return_type(self):
        result = task_func()
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], float)
        self.assertIn(result[1], [None, "The accuracy of the SVM classification is below 0.9."])
    def test_warning_setting(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            _, _ = task_func()
            if w:
                self.assertEqual(str(w[-1].message), "The accuracy of the SVM classification is below 0.9.")
