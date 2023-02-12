import sqlite3
import datetime


def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))


def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()


# with sqlite3.connect('database.db') as db:
#   query = """SELECT * FROM payments"""
#   cursor.execute(query)
#   sum1 = 0
#   for res in cursor:
#   sum1 += res[1]
#   print(res)
#   print('Total', sum1)

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """ SELECT p.amount, p.payment_date, e.name FROM payments p JOIN expenses e ON p.expense_id = e.id
    WHERE e.name like 'Кредит%' 
    """
    # AND (p.payment_date > %(from)d) and (p.payment_date < %(to)d)
    # """ %{'from': get_timestamp(2022, 2, 1), 'to': get_timestamp(2022, 3, 31)}
    cursor.execute(query)
    sum = 0
    for res in cursor:
        sum += res[0]
        print(res)
    print('Total', sum)
