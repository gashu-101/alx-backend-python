import mysql.connector
import csv
import uuid
from mysql.connector import Error

def connect_db():
    """Connect to the MySQL database server."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_database(connection):
    """Create the database ALX_prodev if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        print("Database ALX_prodev created successfully or already exists.")
    except Error as e:
        print(f"Error: {e}")

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='ALX_prodev'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_table(connection):
    """Create the table user_data if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                age DECIMAL(3, 0) NOT NULL
            );
        """)
        print("Table user_data created successfully.")
    except Error as e:
        print(f"Error: {e}")

def insert_data(connection, csv_file):
    """Insert data into the database from the CSV file."""
    try:
        cursor = connection.cursor()
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']
                cursor.execute(
                    """
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE name = VALUES(name);
                    """,
                    (user_id, name, email, age)
                )
        connection.commit()
        print("Data inserted successfully.")
    except Error as e:
        print(f"Error: {e}")

def stream_data(connection):
    """Generator to stream rows from the user_data table."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data;")
        for row in cursor:
            yield row
    except Error as e:
        print(f"Error: {e}")

# Example usage
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
