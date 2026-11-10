import sqlite3

conn = sqlite3.connect("data/instamart.db")

cursor = conn.execute("PRAGMA table_info(orders)")

print("ORDERS TABLE COLUMNS:")

for column in cursor.fetchall():
    print(column[1])

conn.close()