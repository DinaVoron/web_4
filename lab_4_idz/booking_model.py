import pandas as pd


def get_room_type_info(status, conn):
    df = pd.read_sql('''
            SELECT type_room_name as 'Тип_номера',
            COUNT (room_booking_id) as 'Количество',
            CASE
                WHEN COUNT (room_booking_id) > 6
                    THEN 'Высокий'
                WHEN COUNT (room_booking_id) > 4
                    THEN 'Средний'
                WHEN COUNT (room_booking_id) = 0
                    THEN '-'
                ELSE 'Низкий'
            END as 'Спрос'
            FROM type_room
            LEFT OUTER JOIN room
            ON type_room.type_room_id = room.type_room_id
            LEFT OUTER JOIN room_booking
            ON room_booking.room_id = room.room_id
            WHERE status_id = :status_id OR status_id IS NULL
            GROUP BY type_room_name
            ORDER BY 2 DESC, 1
        ''', conn, params={"status_id": status})
    return df

def get_status(conn):
    df = pd.read_sql('''
        SELECT status_id, status_name
        FROM status
    ''', conn)
    return df
