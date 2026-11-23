from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'testdir_task_func'
        os.makedirs(self.test_dir, exist_ok=True)
        f = open(self.test_dir + '/sample1.txt', 'w')
        f.write('Hello, world!')
        f.close()
        f = open(self.test_dir + '/sample2.txt', 'w')
        f.write('The quick brown fox jumps over the lazy dog .')
        f.close()
        f = open(self.test_dir + '/sample3.txt', 'w')
        f.write('NLTK is a leading platform for building Python programs to work with human language data.')
        f.close()
        f = open(self.test_dir + '/sample4.txt', 'w')
        f.write('OpenAI is an organization focused on    ensuring that artificial general intelligence benefits all   of humanity    .')
        f.close()
        f = open(self.test_dir + '/sample5.txt', 'w')
        f.write('Python is an interpreted, high-level , general-purpose programming language.')
        f.close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_case_1(self):
        tokens = task_func(self.test_dir + '/sample1.txt')
        self.assertEqual(tokens, ['Hello', ',', 'world', '!'])

    def test_case_2(self):
        tokens = task_func(self.test_dir + '/sample2.txt')
        self.assertEqual(tokens, ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', '.'])

    def test_case_3(self):
        tokens = task_func(self.test_dir + '/sample3.txt')
        self.assertEqual(tokens, ['NLTK', 'is', 'a', 'leading', 'platform', 'for', 'building', 'Python', 'programs', 'to', 'work', 'with', 'human', 'language', 'data', '.'])
