import sqlite3

def setup_database():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            device_id INTEGER PRIMARY KEY AUTOINCREMENT,
            uuid TEXT,
            region TEXT,
            device_type TEXT,
            ip_address TEXT,
            serial_number TEXT,
            company TEXT,
            department TEXT
        )
    """)
    connection.commit()
    return connection, cursor

def insert_data(connection, cursor, data):
    insert_statement = "INSERT INTO assets (uuid, region, device_type, ip_address, serial_number, company, department) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.executemany(insert_statement, data)
    connection.commit()
    