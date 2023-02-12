import sqlite3
import datetime

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER, 
            name TEXT
    ) """
    cursor.execute(query)

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query1 = """CREATE TABLE IF NOT EXISTS payments(
            id INTEGER, 
            amount REAL,
            payment_date INTEGER,
            expense_id INTEGER
    ) """
    cursor.execute(query1)