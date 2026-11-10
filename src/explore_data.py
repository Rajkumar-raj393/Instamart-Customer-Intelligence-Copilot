from pathlib import Path
import pandas as pd

# Project data location
DATA_PATH = Path("data/raw")

files = [
    "customers.csv",
    "products.csv",
    "orders.csv",
    "tickets.csv",
    "policy_eval.csv",
    "agent_scenarios.csv"
]

for filename in files:
    print("\n" + "=" * 50)
    print("FILE:", filename)

    df = pd.read_csv(DATA_PATH / filename)

    print("Rows and columns:", df.shape)
    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nFirst 5 records:")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:", df.duplicated().sum())

print("\nDATA EXPLORATION COMPLETED!")