from jinja2 import Template
import sqlite3
import library_model as lm

# устанавливаем соединение с базой данных
conn = sqlite3.connect("library.sqlite")
# выбираем записи из таблицы publisher
df_publisher = lm.get_publisher(conn)
df_genre = lm.get_genre(conn)
df_reader = lm.get_reader(conn)
df_author = lm.get_author(conn)
df_book_author = lm.get_book_author(conn)
df_book = lm.get_book(conn)
df_book_reader = lm.get_book_reader(conn)
# закрываем соединение с базой
conn.close()
# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open('library_templ.html', 'r', encoding='utf-8')
html = f_template.read()
f_template.close()
# создаем объект-шаблон
template = Template(html)
# генерируем результат на основе шаблона
result_html = template.render(
    table_1="publisher",
    relation_1=df_publisher,
    table_2="genre",
    relation_2=df_genre,
    table_3="reader",
    relation_3=df_reader,
    table_4="author",
    relation_4=df_author,
    table_5="book_author",
    relation_5=df_book_author,
    table_6="book",
    relation_6=df_book,
    table_7="book_reader",
    relation_7=df_book_reader,
    len=len
)
# создаем файл для HTML-страницы
f = open('library.html', 'w', encoding='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
