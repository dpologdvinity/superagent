from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import shutil
import os
import doctest
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_directory = f'{self.base_tmp_dir}/test/'
        if not os.path.exists(self.test_directory):
            os.makedirs(self.test_directory)
        test_data = {'file_1.docx': 'This is a sample text without any double quotes.', 'file_2.docx': 'This is a "sample" text with double quotes.', 'file_3.docx': 'This is a \\"sample\\" text with double quotes already protected.', 'file_4.docx': 'Hello "world"! How are you "today"?', 'file_5.docx': 'Testing "multiple" paragraphs.\n\nAnother paragraph with "quotes".'}
        for file_name, content in test_data.items():
            doc = Document()
            for paragraph in content.split('\n'):
                doc.add_paragraph(paragraph)
            doc.save(self.test_directory + file_name)

    def tearDown(self):
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)

    def read_docx_content(self, file_path):
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])

    def test_case_1(self):
        result = task_func(self.test_directory)
        self.assertEqual(result, 5)
        content = self.read_docx_content(self.test_directory + 'file_1.docx')
        self.assertEqual(content, 'This is a sample text without any double quotes.')

    def test_case_2(self):
        result = task_func(self.test_directory)
        self.assertEqual(result, 5)
        content = self.read_docx_content(self.test_directory + 'file_2.docx')
        self.assertEqual(content, 'This is a \\"sample\\" text with double quotes.')

    def test_case_3(self):
        result = task_func(self.test_directory)
        self.assertEqual(result, 5)
        content = self.read_docx_content(self.test_directory + 'file_3.docx')
        self.assertEqual(content, 'This is a \\"sample\\" text with double quotes already protected.')
