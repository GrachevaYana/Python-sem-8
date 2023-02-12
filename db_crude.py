import sqlite3
import datetime

def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query1 = """INSERT INTO     expenses(id, name)     VALUES (1,'Коммуналка')"""
    query2 = """INSERT INTO     expenses(id, name)     VALUES (2,'Кредит1')"""
    # cursor.execute(query1)
    # cursor.execute(query2)
    # db.commit()

insert_payments = [
    (1, 12000, get_timestamp(2022, 1, 10), 1),
    (2, 110000, get_timestamp(2022, 1, 12), 2),
    (3, 11000, get_timestamp(2022, 2, 10), 1),
    (4, 110000, get_timestamp(2022, 2, 12), 2),
    (5, 10000, get_timestamp(2022, 3, 10), 1),
    (6, 110000, get_timestamp(2022, 3, 12), 2),
    (7, 9000, get_timestamp(2022, 4, 10), 1),
    (8, 110000, get_timestamp(2022, 4, 12), 2),
    (9, 8000, get_timestamp(2022, 5, 10), 1),
    (10, 100000, get_timestamp(2022, 5, 10), 2)
]
with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query3 = """INSERT INTO     payments(id, amount, payment_date, expense_id)     VALUES (?,?,?,?);"""
    # cursor.executemany(query3, insert_payments)
    # db.commit()
    # print(cursor.rowcount, "строк")

# with sqlite3.connect('database.db') as db:
#     cursor = db.cursor()
#     query3 = """UPDATE expenses SET  """

# ФУНКЦИЯ ДЛЯ ОБНОВЛЕНИЯ ЗАПИСЕЙ
def update_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """UPDATE expenses SET name = 'Кредит' WHERE name = 'Кредит1' """
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print('Количество записей: ', cursor.rowcount, 'успешно обновлено')
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

update_sqlite_table()



