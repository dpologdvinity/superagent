from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        self.texts = ['Hello, world!', 'Data science is about the extraction of knowledge from data.', 'Machine learning is a fascinating field.', 'Python is a versatile programming language.', 'Stop words are filtered out in text preprocessing.']

    def test_dtm_shape(self):
        """Ensure the DTM has the correct shape."""
        dtm = task_func(self.texts)
        self.assertEqual(dtm.shape[0], len(self.texts), 'DTM should have one row per document.')

    def test_dtm_non_negative(self):
        """Ensure all values in the DTM are non-negative."""
        dtm = task_func(self.texts)
        self.assertTrue((dtm >= 0).all().all(), 'All DTM values should be non-negative.')

    def test_stopwords_removal(self):
        """Check if common stopwords are removed."""
        dtm = task_func(['This is a test.', 'Another test here.'])
        self.assertNotIn('is', dtm.columns, 'Stopwords should be removed from DTM columns.')
