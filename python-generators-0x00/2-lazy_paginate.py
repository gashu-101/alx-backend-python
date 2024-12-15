from seed import connect_to_prodev

def paginate_users(page_size, offset):
    """
    Fetches a page of users from the user_data table.

    :param page_size: Number of rows to fetch in each page
    :param offset: Offset to start fetching rows from
    :return: List of user rows
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset};")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """
    Generator function that lazily fetches pages of users from the database.

    :param page_size: Number of rows to fetch per page
    :yield: A page of user rows
    """
    offset = 0

    while True:
        page = paginate_users(page_size, offset)
        if not page:  # Stop if no more data is fetched
            break
        yield page
        offset += page_size
