from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        """Set up common test data and secret key."""
        self.secret_key = 'test_secret_key'

    def compute_expected_signature(self, req_data):
        """Compute the expected HMAC signature for comparison in tests."""
        json_req_data = json.dumps(req_data)
        hmac_obj = hmac.new(self.secret_key.encode(), json_req_data.encode(), hashlib.sha256)
        hmac_hex = hmac_obj.hexdigest()
        url_encoded_signature = urllib.parse.quote_plus(hmac_hex)
        return url_encoded_signature

    def test_return_type(self):
        """Ensure the function returns a string."""
        result = task_func({'key': 'value'}, self.secret_key)
        self.assertIsInstance(result, str)

    def test_known_data_signature(self):
        """Validate the HMAC signature against a known output for specific data."""
        known_data = {'known': 'data'}
        expected_signature = self.compute_expected_signature(known_data)
        result = task_func(known_data, self.secret_key)
        self.assertEqual(result, expected_signature)

    def test_empty_data(self):
        """Verify the function behaves correctly with empty input data."""
        result = task_func({}, self.secret_key)
        expected_signature_for_empty_data = self.compute_expected_signature({})
        self.assertEqual(result, expected_signature_for_empty_data)
