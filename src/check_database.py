import sqlite3

connection = sqlite3.connect("data/instamart.db")
cursor = connection.cursor()

tables = ["customers", "orders", "products", "tickets"]

print("DATABASE VERIFICATION\n")

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count} records")

# Check database integrity
cursor.execute("PRAGMA integrity_check")
print("\nDatabase integrity:", cursor.fetchone()[0])

connection.close()