import mysql.connector
from mysql.connector import Error

def stream_users():
    """
    Generator function that fetches rows one by one from the user_data table.
    """
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='my_password',
            database='ALX_prodev'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)  # Fetch rows as dictionaries
            cursor.execute("SELECT * FROM user_data;")

            # Yield each row one at a time
            for row in cursor:
                yield row

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error: {e}")
