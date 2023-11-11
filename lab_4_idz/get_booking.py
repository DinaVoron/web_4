import sqlite3
from jinja2 import Template
from booking_model import get_room_type_info, get_status

status_id = 1
is_none = False

conn = sqlite3.connect('booking.sqlite')
df_booking = get_room_type_info(status_id, conn)
df_status = get_status(conn)
conn.close()


f_temp = open('booking_temp.html', 'r', encoding='utf-8')
html = f_temp.read()
f_temp.close()

template = Template(html)
result_html = template.render(
    df_booking=df_booking,
    df_status=df_status,
    status=status_id,
    is_none=is_none,
    len=len
)

f_res = open('booking.html', 'w', encoding='utf-8')
f_res.write(result_html)
f_res.close()
