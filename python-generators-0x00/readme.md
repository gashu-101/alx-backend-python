# ALX Backend Python Project Documentation

## Overview

This project demonstrates how to interact with a MySQL database using Python. It includes functions to connect to the database, create a database and table, insert data from a CSV file, and stream data from the table using a generator.

## Requirements

- Python 3.x
- MySQL server
- `mysql-connector-python` library
- `csv` module
- `uuid` module

## Installation

1. Install the MySQL server and create a user with the necessary privileges.
2. Install the required Python libraries:
   ```sh
   pip install mysql-connector-python
   ```

## Usage

1. **Connect to the MySQL database server:**

   ```python
   connection = connect_db()
   ```

2. **Create the database `ALX_prodev` if it does not exist:**

   ```python
   create_database(connection)
   ```

3. **Connect to the `ALX_prodev` database:**

   ```python
   connection = connect_to_prodev()
   ```

4. **Create the table `user_data` if it does not exist:**

   ```python
   create_table(connection)
   ```

5. **Insert data into the database from a CSV file:**

   ```python
   insert_data(connection, 'user_data.csv')
   ```

6. **Stream rows from the `user_data` table:**
   ```python
   for row in stream_data(connection):
       print(row)
   ```

## Example

```python
if __name__ == "__main__":
    connection = connect_db()
    if connection:
        create_database(connection)
        connection.close()

        connection = connect_to_prodev()
        if connection:
            create_table(connection)
            insert_data(connection, 'user_data.csv')

            print("Streaming data:")
            for row in stream_data(connection):
                print(row)

            connection.close()
```

## Functions

- `connect_db()`: Connects to the MySQL database server.
- `create_database(connection)`: Creates the database `ALX_prodev` if it does not exist.
- `connect_to_prodev()`: Connects to the `ALX_prodev` database.
- `create_table(connection)`: Creates the table `user_data` if it does not exist.
- `insert_data(connection, csv_file)`: Inserts data into the database from the CSV file.
- `stream_data(connection)`: Generator to stream rows from the `user_data` table.

## Notes

- Ensure that the MySQL server is running and accessible.
- Replace the placeholder values for `user` and `password` with your actual MySQL credentials.
- The CSV file should have columns: `name`, `email`, and `age`.
