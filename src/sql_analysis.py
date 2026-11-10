import sqlite3

connection = sqlite3.connect("data/instamart.db")
cursor = connection.cursor()

print("INSTAMART SQL ANALYSIS")
print("----------------------")

# Query 1: Total customers
cursor.execute("SELECT COUNT(*) FROM customers")
print("Total customers:", cursor.fetchone()[0])

# Query 2: Total products
cursor.execute("SELECT COUNT(*) FROM products")
print("Total products:", cursor.fetchone()[0])

# Query 3: Orders by status
cursor.execute("""
    SELECT status, COUNT(*)
    FROM orders
    GROUP BY status
""")

print("\nOrders by status:")
for row in cursor.fetchall():
    print(row[0], ":", row[1])

# Query 4: Customers by city
cursor.execute("""
    SELECT city, COUNT(*)
    FROM customers
    GROUP BY city
    ORDER BY COUNT(*) DESC
""")

print("\nCustomers by city:")
for row in cursor.fetchall():
    print(row[0], ":", row[1])

connection.close()

print("\nSQL ANALYSIS COMPLETED!")