import pandas as pd


def get_reader(conn):
    df = pd.read_sql('''
        SELECT reader_id, reader_name
        FROM reader
    ''', conn)
    return df


def get_book_reader(conn, id):
    df = pd.read_sql('''
        WITH get_author(book_id, title, authors) AS (
            SELECT book_id, title, GROUP_CONCAT(author_name, ', ')
            FROM book
            JOIN book_author
            USING(book_id)
            JOIN author
            USING(author_id)
            GROUP BY book_id
        )
        SELECT DISTINCT title as 'Название', authors as 'Авторы', borrow_date as 'Дата_выдачи', return_date as 'Дата_возврата'
        FROM book_reader
        JOIN get_author
        USING(book_id)
        WHERE reader_id = :id
        ORDER BY title
    ''', conn, params={"id": id})
    return df
