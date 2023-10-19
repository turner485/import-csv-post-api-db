import unittest
import sqlite3
from unittest.mock import patch, Mock, mock_open
import tempfile  # Import tempfile
from io import StringIO
from main import read_csv_and_filter, main

temp_csv_file = tempfile.NamedTemporaryFile(delete=False)

mock_data = []

for i in range(1000):
    # Generate mock data for each line
    line_data = {
        'uuid': f'uuid_{i}',
        'region': f'region_{i}',
        'device_type': f'device_type_{i}',
        'ip_address': f'ip_address_{i}',
        'serial_number': f'serial_number_{i}',
        'company': f'company_{i}',
        'department': f'department_{i}'
    }
    mock_data.append(line_data)

class TestMain(unittest.TestCase):
    @patch('main.open', create=True)
    @patch('main.csv.reader')
    def test_read_csv_and_filter(self, csv_reader_mock, open_mock):
        csv_reader_mock.return_value = mock_data

        # Call the function
        result = read_csv_and_filter("test_salt", "test_file.csv")

        # Validate the result
        self.assertEqual(len(result), len(mock_data))  # Check if the function returns the expected number of rows0

    @patch('main.open', create=True)
    @patch('main.csv.reader')
    @patch('main.sqlite3.connect')
    @patch('main.send_data_to_api')
    def test_main(self, send_data_mock, sqlite_connect_mock, csv_reader_mock, open_mock):
        csv_reader_mock.return_value = [["row1", "data1"], ["row2", "data2"]]
        open_mock.return_value.__enter__.return_value = StringIO()
        
        # Mock the database connection and cursor
        connection_mock = sqlite_connect_mock.return_value
        cursor_mock = connection_mock.cursor.return_value
        cursor_mock.fetchall.return_value = [("data1", "data2"), ("data3", "data4")]
        send_data_mock.return_value.status_code = 201  # Set the status code for a successful request
          
        args = Mock(csv_file=temp_csv_file.name)
        try:
            main(args)
        finally:
            temp_csv_file.close()
      

if __name__ == '__main__':
    unittest.main()