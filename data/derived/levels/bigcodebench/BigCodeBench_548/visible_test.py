from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        random.seed(1)
        result = task_func()
        self.assertEqual(result, 'eJwFwUEOhCAMAMAvLVBXONJooGqkUCDa/z/EmR3M0epjNwQ2sSr5P8a+3pkxcyPK9YwwnhRgv1RXdu85F5CJZEvq+t4sVkpD1DBLkmA6kPhRj+6jdcvPyeAPdLQbtg==')

    def test_case_2(self):
        random.seed(0)
        result = task_func(50)
        self.assertEqual(result, 'eJwzMQzwCvY38g4KMwv2Ngz3MrM0NvMxMIsMdAkIM7MIMvUyCnGM8jeOdAwy9fQxdQ/1tAAAVX8NdQ==')

    def test_case_3(self):
        random.seed(42)
        result = task_func(200)
        self.assertEqual(result, 'eJwFwVkCQCAQANArRZs+WzCTJIyU+x/Ee81GZF2F4uC20Agqt/zbl2kPQVTOyGTir3w+h5vHsL05Q9StrmzJpj1dDOhSBC1TO9QZ8YlVHWDu4MI7Fp8NTcJ+nWKbyznJeK9Kbq0uA41kk9WSJy+ncPlhmC+KsgAxSKaVe8a9IvgXlfDYYdbPNfI1lHKybsKxS1zPsqEukpwRP8dcNyU=')
