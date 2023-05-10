"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

"""пустые списки для чтения файлов csv"""
result_employees = []
result_customer = []
result_orders = []

"""Пути до файлов csv"""
way_employees = '/Users/ralina/Desktop/все проекты/postgres-homeworks/homework-1/north_data/employees_data.csv'
way_custom = '/Users/ralina/Desktop/все проекты/postgres-homeworks/homework-1/north_data/customers_data.csv'
way_orders = '/Users/ralina/Desktop/все проекты/postgres-homeworks/homework-1/north_data/orders_data.csv' \

"""Чтение файла csv"""
with open(way_employees, newline='') as File:
    reader = csv.reader(File)
    result_employees.extend(reader)

with open(way_custom, newline='') as File:
    reader = csv.reader(File)
    result_customer.extend(reader)

with open(way_orders, newline='') as File:
    reader = csv.reader(File)
    result_orders.extend(reader)

"""Конект к БД"""
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='Ralina:11'
)

"""Создаем курсор"""
id = 1
cur = conn.cursor()
for row in result_employees:
    if row[0] == "first_name":
        continue
    row.insert(0, id)
    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
    cur.execute("SELECT * FROM employees")
    conn.commit()
    id += 1
rows = cur.fetchall()
for row in rows:
    print(row)

for row in result_customer:
    if row[0] == "customer_id":
        continue
    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
    cur.execute("SELECT * FROM customers")
    conn.commit()
rows = cur.fetchall()
for row in rows:
    print(row)

for row in result_orders:
    if row[0] == "order_id":
        continue
    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)
    cur.execute("SELECT * FROM orders")
    conn.commit()
rows = cur.fetchall()
for row in rows:
    print(row)





