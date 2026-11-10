import pandas as pd

# Load cleaned support tickets
df = pd.read_csv(
    "data/processed/tickets_clean.csv"
)

print("SUPPORT TICKET ANALYSIS")
print("-----------------------")

print("\nTotal tickets:", len(df))

print("\nAvailable columns:")
print(df.columns.tolist())

print("\nTicket category distribution:")
print(df["category"].value_counts(dropna=False))

print("\nTicket priority distribution:")
if "priority" in df.columns:
    print(df["priority"].value_counts(dropna=False))

print("\nSample support tickets:")
print(df.head(10).to_string(index=False))

print("\nTICKET EXPLORATION COMPLETED!")