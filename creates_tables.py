import sqlite3

connection = sqlite3.connect('burgers.db')
cursor = connection.cursor()

create_table = "CREATE TABLE customers (id INT, username VARCHAR(20), password VARCHAR(20))"
cursor.execute(create_table)

create_table = "CREATE TABLE burgers (name VARCHAR(20), price smallmoney, type VARCHAR(20))"
cursor.execute(create_table)

connection.commit()
connection.close()