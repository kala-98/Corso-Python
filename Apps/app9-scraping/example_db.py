import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor() # cursor's creation

# query
cursor.execute("SELECT * FROM events")

rows = cursor.fetchall()

print(rows)
