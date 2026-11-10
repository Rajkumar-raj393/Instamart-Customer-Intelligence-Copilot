from pathlib import Path
import sqlite3
import pandas as pd

database_path = Path("data/instamart.db")

tables = {
    "customers": "data/processed/customers_clean.csv",
    "orders": "data/processed/orders_clean.csv",
    "products": "data/processed/products_clean.csv",
    "tickets": "data/processed/tickets_clean.csv"
}

# Connect to SQLite database
connection = sqlite3.connect(database_path)

# Import each cleaned CSV into SQLite
for table_name, csv_path in tables.items():
    df = pd.read_csv(csv_path)

    df.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )

    print(f"{table_name}: {len(df)} rows imported")

# Check database tables
cursor = connection.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
""")

print("\nDatabase tables:")
for table in cursor.fetchall():
    print(table[0])

connection.close()

print("\nDATABASE CREATED SUCCESSFULLY!")