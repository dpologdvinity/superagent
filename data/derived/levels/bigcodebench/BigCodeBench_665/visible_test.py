from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def base(self, src_dir, dst_dir):
        if os.path.exists(src_dir):
            shutil.rmtree(src_dir)
        os.mkdir(src_dir)
        os.mkdir(dst_dir)
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join(src_dir, filename), 'w') as f:
                f.write('test')
        task_func(src_dir, dst_dir)
        for d in [src_dir, dst_dir]:
            self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
            self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
            self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
            self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))
            self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
            self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
            if d == src_dir:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
            else:
                self.assertFalse(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertFalse(os.path.exists(os.path.join(d, 'a.doc')))

    def tearDown(self):
        for d in ['./source', './destination', './src', './dst', './s', './d']:
            if os.path.exists(d):
                shutil.rmtree(d)

    def test_case_1(self):
        self.base('./source', './destination')

    def test_case_2(self):
        self.base('./src', './dst')

    def test_case_3(self):
        self.base('./s', './d')
