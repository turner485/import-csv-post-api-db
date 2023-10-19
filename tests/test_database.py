import unittest
from unittest.mock import patch, Mock
from database import setup_database, insert_data

class TestDatabase(unittest.TestCase):
    @patch('database.sqlite3.connect')
    def test_setup_database(self, connect_mock):
        connection_mock = Mock()
        cursor_mock = Mock()
        connect_mock.return_value = (connection_mock, cursor_mock)
        connection, cursor = setup_database()
        self.assertEqual(connection, connection_mock)  # Check if the function returns the expected connection
        self.assertEqual(cursor, cursor_mock)  # Check if the function returns the expected cursor

    @patch('main.sqlite3.connect')
    def test_insert_data(self, sqlite_connect_mock):
        connection_mock = sqlite_connect_mock.return_value
        cursor_mock = connection_mock.cursor.return_value

        # Create a sample dataset with values for all columns
        data = [
            ('uuid', 'US', 'PC', '192.168.1.1', 'serial', 'company', 'department')
        ]

        # Call insert_data directly, not through main object
        main.database.insert_data(cursor_mock, data)

        cursor_mock.executemany.assert_called_with(
            'INSERT INTO assets (uuid, region, device_type, ip_address, serial_number, company, department) VALUES (?, ?, ?, ?, ?, ?, ?)',
            data  # Make sure you pass the data as a list of tuples
        )

if __name__ == '__main__':
    unittest.main()