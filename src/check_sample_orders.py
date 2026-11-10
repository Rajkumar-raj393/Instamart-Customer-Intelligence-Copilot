import sqlite3

conn = sqlite3.connect("data/instamart.db")

cursor = conn.execute("""
    SELECT order_id, status, order_amount, delivery_minutes
    FROM orders
    WHERE status = 'completed'
      AND order_amount > 1000
      AND delivery_minutes > 45
    LIMIT 10
""")

print("ORDERS REQUIRING HUMAN APPROVAL:")

for row in cursor.fetchall():
    print(row)

conn.close()