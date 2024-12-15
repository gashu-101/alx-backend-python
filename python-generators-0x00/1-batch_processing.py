import mysql.connector
from mysql.connector import Error

def stream_users_in_batches(batch_size):
    """
    Generator function that fetches rows in batches from the user_data table.
    
    :param batch_size: Number of rows to fetch in each batch
    :return: Yields each batch of rows
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='ALX_prodev'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT COUNT(*) AS total FROM user_data;")
            total_records = cursor.fetchone()['total']

            for offset in range(0, total_records, batch_size):
                cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset};")
                batch = cursor.fetchall()
                if batch:
                    yield batch

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error: {e}")


def batch_processing(batch_size):
    """
    Processes each batch by filtering users over the age of 25 and prints them.
    
    :param batch_size: Number of rows to process in each batch
    """
    for batch in stream_users_in_batches(batch_size):
        filtered_users = (user for user in batch if user['age'] > 25)
        for user in filtered_users:
            print(user)
