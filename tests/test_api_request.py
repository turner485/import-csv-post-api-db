import unittest
from unittest.mock import patch, Mock
from api_request import send_data_to_api

class TestApiRequests(unittest.TestCase):
    @patch('api_request.requests.post', return_value=Mock(status_code=201))
    def test_send_data_to_api(self, post_mock):
        api_url = "https://example.com/api"
        data = {"key": "value"}
        response = send_data_to_api(api_url, data)
        self.assertEqual(response.status_code, 201)  # Check if the function returns the expected status code

if __name__ == '__main__':
    unittest.main()