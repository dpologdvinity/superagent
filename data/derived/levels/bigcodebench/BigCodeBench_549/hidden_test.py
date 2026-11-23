from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from io import StringIO
class TestCases(unittest.TestCase):
    def test_encode_basic_dataframe(self):
        df = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        encoded_df = task_func(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
    def test_encode_with_different_columns(self):
        df = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
        encoded_df = task_func(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
    def test_encode_empty_dataframe(self):
        df = {'X': [], 'Y': []}
        encoded_df = task_func(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv, check_dtype=False, check_index_type=False)
    def test_encode_with_specific_values(self):
        df = {'ID': [101, 102, 103], 'Score': [85, 90, 88]}
        encoded_df = task_func(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
    def test_encode_with_string_values(self):
        df = {'City': ['NY', 'LA'], 'Population': [8000000, 4000000]}
        encoded_df = task_func(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
