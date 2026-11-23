from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        example_str = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
        ax, top_n_words = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
        # Test the number of words in the plot
        self.assertEqual(len(ax.get_xticklabels()), 4, "The number of words in the plot is not 30.")
        # Test the top_n_words dictionary
        self.assertEqual(top_n_words, {'Smith': 2, 'Josie': 1, 'Mugsy': 1, 'Dog': 1}, "The top_n_words dictionary is incorrect.")
    def test_case_2(self):
        example_str = "Hello [1234 STREET, CITY, STATE 12345] World [5678 LANE, TOWN, PROVINCE 67890]"
        ax, _ = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
    def test_case_3(self):
        example_str = "[IGNORE THIS] This is a simple test string [ANOTHER IGNORE]"
        ax, top_n_words = task_func(example_str, top_n=5)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
        # Test the histogram data
        #self.assertEqual(len(ax.patches), 5, "The number of words in the plot is not 5.")
        # Test the top_n_words dictionary
        self.assertEqual(top_n_words, {'This': 1, 'is': 1, 'a': 1, 'simple': 1, 'test': 1}, "The top_n_words dictionary is incorrect.")
    
    def test_case_4(self):
        example_str = "[BEGIN] Testing the function with different [MIDDLE] types of input strings [END]"
        ax, _ = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
    
    def test_case_5(self):
        example_str = "Example without any brackets so all words should be considered."
        ax, _ = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
