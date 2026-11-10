import pandas as pd

# Load cleaned support tickets
df = pd.read_csv(
    "data/processed/tickets_clean.csv"
)

print("SUPPORT TICKET ANALYSIS")
print("-----------------------")

# Total tickets
print("\nTotal tickets:", len(df))

# Display column names
print("\nAvailable columns:")
print(df.columns.tolist())

# Display category distribution
if "category" in df.columns:
    print("\nTicket category distribution:")
    print(df["category"].value_counts(dropna=False))

# Display priority distribution
if "priority" in df.columns:
    print("\nTicket priority distribution:")
    print(df["priority"].value_counts(dropna=False))
else:
    print("\nPriority column not available.")

# Display sample tickets
print("\nSample support tickets:")
print(df.head(10).to_string(index=False))

print("\nTICKET EXPLORATION COMPLETED!")