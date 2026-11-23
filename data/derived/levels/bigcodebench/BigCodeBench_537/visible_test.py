from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
import os
import sqlite3
import matplotlib.pyplot as plt
import tempfile

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.alt_db_path = os.path.join(self.test_dir.name, 'test_alt.db')
        conn = sqlite3.connect(self.alt_db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE People (name TEXT, age INT)')
        cursor.executemany('INSERT INTO People VALUES (?, ?)', [('Alice', 25), ('Bob', 30)])
        conn.commit()
        conn.close()
        self.default_db_path = os.path.join(self.test_dir.name, 'test.db')
        conn = sqlite3.connect(self.default_db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE Employees (name TEXT, age INT)')
        cursor.executemany('INSERT INTO Employees VALUES (?, ?)', [('Charlie', 35), ('David', 40)])
        conn.commit()
        conn.close()
        self.multiple_db_path = os.path.join(self.test_dir.name, 'test_multiple.db')
        conn = sqlite3.connect(self.multiple_db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE MultipleAge (name TEXT, age INT)')
        cursor.executemany('INSERT INTO MultipleAge VALUES (?, ?)', [('Alice', 25), ('Bob', 30), ('Charlie', 35)])
        conn.commit()
        conn.close()
        self.negative_age_db_path = os.path.join(self.test_dir.name, 'test_negative_age.db')
        conn = sqlite3.connect(self.negative_age_db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE NegativeAge (name TEXT, age INT)')
        cursor.executemany('INSERT INTO NegativeAge VALUES (?, ?)', [('Eve', -1), ('Frank', 20)])
        conn.commit()
        conn.close()
        self.empty_db_path = os.path.join(self.test_dir.name, 'test_empty.db')
        conn = sqlite3.connect(self.empty_db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE EmptyAge (name TEXT, age INT)')
        conn.commit()
        conn.close()

    def tearDown(self):
        self.test_dir.cleanup()
        plt.close('all')

    def _check_plot(self, ax, contains_data=True):
        self.assertTrue(isinstance(ax, plt.Axes), 'The plot should be an Axes object.')
        self.assertEqual(ax.get_xlabel(), 'age', "The x-axis label should be 'age'.")
        if contains_data:
            self.assertTrue(len(ax.lines) > 0, 'The plot should contain a KDE line.')

    def test_case_1(self):
        ax = task_func(db_name=self.default_db_path, table_name='Employees')
        self._check_plot(ax)

    def test_case_2(self):
        ax = task_func(db_name=self.alt_db_path)
        self._check_plot(ax)

    def test_case_3(self):
        ax = task_func(db_name=self.default_db_path, table_name='Employees')
        self._check_plot(ax)
