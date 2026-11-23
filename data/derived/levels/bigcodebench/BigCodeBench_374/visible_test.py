from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import shutil
from openpyxl import load_workbook, Workbook
import doctest
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_directory = f'{self.base_tmp_dir}/test/'
        os.makedirs(self.test_directory, exist_ok=True)
        file_data = [{'filename': 'file1.xlsx', 'sheets': {'Sheet1': [['Hello', 'World', 'This is a "test" string.'], ['Another', 'Row with "quotes"', 'And "more" quotes.']]}}, {'filename': 'file2.xlsx', 'sheets': {'Sheet1': [['Just a', 'Normal row.', 'Nothing special.'], ['Another', 'normal row.', 'Still nothing special.']], 'Sheet2': [['Sheet2 data.', 'Another "quoted" string.', 'End of row.']]}}, {'filename': 'file3.xlsx', 'sheets': {'Sheet1': [['A simple', 'row without', 'any quotes.']]}}]
        for file_info in file_data:
            workbook = Workbook()
            workbook.remove(workbook.active)
            for sheet_name, rows in file_info['sheets'].items():
                sheet = workbook.create_sheet(title=sheet_name)
                for row in rows:
                    sheet.append(row)
            workbook.save(filename=os.path.join(self.test_directory, file_info['filename']))

    def tearDown(self):
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)

    def test_case_1(self):
        processed_files_count = task_func(directory_path=self.test_directory)
        self.assertEqual(processed_files_count, 3)
        workbook = load_workbook(filename=os.path.join(self.test_directory, 'file1.xlsx'))
        sheet = workbook.active
        self.assertEqual(sheet.cell(row=1, column=3).value, 'This is a \\"test\\" string.')
        self.assertEqual(sheet.cell(row=2, column=2).value, 'Row with \\"quotes\\"')
        self.assertEqual(sheet.cell(row=2, column=3).value, 'And \\"more\\" quotes.')

    def test_case_2(self):
        workbook = load_workbook(filename=os.path.join(self.test_directory, 'file2.xlsx'))
        sheet1 = workbook['Sheet1']
        self.assertEqual(sheet1.cell(row=1, column=1).value, 'Just a')
        sheet2 = workbook['Sheet2']
        self.assertEqual(sheet2.cell(row=1, column=2).value, 'Another "quoted" string.')

    def test_case_3(self):
        workbook = load_workbook(filename=os.path.join(self.test_directory, 'file3.xlsx'))
        sheet = workbook.active
        self.assertEqual(sheet.cell(row=1, column=1).value, 'A simple')
