from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os

class TestCases(unittest.TestCase):

    def setUp(self):
        self.filenames = []
        for i in range(1, 7):
            self.filenames.append('task_func_test_output_' + str(i) + '.txt')

    def tearDown(self):
        for filename in self.filenames:
            if os.path.exists(filename):
                os.remove(filename)

    def test_case_1(self):
        text = '$abc def $efg $hij klm $ $abc $abc $hij $hij'
        filename = self.filenames[0]
        expected_words = ['$abc', '$efg', '$hij', '$abc', '$abc', '$hij', '$hij']
        output_path = task_func(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))

    def test_case_2(self):
        text = 'There are no dollar words here.'
        filename = self.filenames[1]
        expected_words = []
        output_path = task_func(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))

    def test_case_3(self):
        text = '$$$$ $$ $$$$ $abc$ $def'
        filename = self.filenames[2]
        expected_words = ['$abc', '$def']
        output_path = task_func(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))
