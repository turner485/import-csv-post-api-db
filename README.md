# Project Name: csv-to-api-data-import

## Description
This GitHub repository houses the code and documentation for a coding challenge solution that involves reading data from a CSV file, setting up database tables, and posting the data to an API endpoint. The project provides a comprehensive solution for efficiently importing structured data into a database while simultaneously pushing it to an external API. It can be used as a reference for similar data import and integration tasks, and it showcases best practices for working with data pipelines and APIs.

## Key Features
CSV data parsing and transformation.
Database table setup and data storage.
API integration for seamless data posting.
Code and documentation for a complete data import workflow.

## Contributions
Contributions and improvements to the project are welcome. Feel free to fork the repository, make enhancements, and submit pull requests.

### License
This project is open-source and is available under the [license name] license. See the LICENSE.md file for details.

This is just a template, so be sure to customize it to match your project's specifics, licensing, and any other relevant information.

### Build
This program is comprised of 4 python files.

1. main.py 
The is where the csv is read in, the lines validated and the salt hash given.
The database tables are being populated in this file.
The assets are also being posted to the API endpoint.

2. database.py
This is where the database connection is being established, there is also a table sql query in this file.

3. api_request.py
This is where the API endpoint post query is established.

4. helpers.py
The ipv4 & md5 validation i added to the helpers folder.

- example.csv
This has all the data for the program in.

### prerequisites
- You will need a machine with Python 3.X
- You will need to install the `requirements.txt`.
- You will need a CLI.

## Usage
- Clone this repository
- Follow the setup instructions in the documentation to configure the database and API.
- Run the provided scripts to perform the data import.
Because this is a CLI program you will need command prompt open to run this.
1. `cd path/to/your/directory/python-coding-challenge`
2. `python main.py --csv-file example.csv`
3. The program will then start running. It will show a few prompts along the way to explain what it is doing.
"# import-csv-post-api-db" 
