import csv
import hashlib
import argparse  
import logging
import json
from helpers import validation_ip, validation_md5
from database import setup_database, insert_data
from api_request import send_data_to_api

# Configure the logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

salt = "10salt$512%#"
api_url = "https://jsonplaceholder.typicode.com/posts"
chunk_size = 75

input("""This is a CLI program that will do the following;
1. Import a csv into a list validating the lines. 
2. Inserting the data to database tables in sqlite3.
3. Posting the data to an API endpoint.
Please press enter to continue...""")

def read_csv_and_filter(salt, csv_file):
    validated_list = []
    logging.info("importing and validating lines from csv...")
    with open(csv_file, 'r') as csv_lines:
        csv_reader = csv.reader(csv_lines)
        for row in csv_reader:
            try: 
                # Assuming that IP address is in column 2 and MD5 hash is in column 3
                ip_check = row[2]
                md5_check = row[3]
            except KeyError:
                pass
            if validation_ip(ip_check) and validation_md5(md5_check):
                logging.info(f"Row passed validation: {row}")
                # Append the row to the filtered list
                row.insert(0, hashlib.sha256(f"{salt}-{md5_check}".encode()).hexdigest())
                validated_list.append(row)
            else:
                logging.warning(f"Row failed validation: {row}")
    return validated_list

def main(args):
    csv_file = args.csv_file
    validated_lines = read_csv_and_filter(salt, csv_file)
    input("Validation complete, Setting up database.\nPlease press enter to continue...")
    connection, cursor = setup_database()
    insert_data(connection, cursor, validated_lines)
     
    # Check if the database is populated
    cursor.execute("SELECT * FROM assets")
    data = cursor.fetchall()
    
    if data:
        for row in data:
            logging.info(row)
    else:
        logging.info("Database is empty.")
        
    connection.close()
    input("""Database and tables populated.
Now establishing connection with API endpoint.
Press enter to continue...""")
    # Split the data into chunks and send each chunk to the API
    for i in range(0, len(validated_lines), chunk_size):
        chunk = validated_lines[i:i+chunk_size]
        data_to_send = {"assets": chunk}
        json_data = json.dumps(data_to_send)
        response = send_data_to_api(api_url, data=json_data)
        
        # Check the response status and handle it as needed
        if response.status_code == 201:
            logging.info("Chunk successfully posted.")
            logging.info(f"Chunk:{json_data}")
        else:
            logging.warning(f"Failed to post chunk. Status code: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV data import and management")
    parser.add_argument('--csv-file', type=str, help="Path to the CSV file")
    args = parser.parse_args()
    main(args)