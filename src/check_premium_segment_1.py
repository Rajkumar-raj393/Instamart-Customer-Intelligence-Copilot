import pandas as pd

features = pd.read_csv("data/processed/customer_features.csv")
segments = pd.read_csv("data/processed/customer_segments.csv")

df = features.merge(segments, on="customer_id")

summary = df.groupby("segment").agg(
    customers=("customer_id", "count"),
    avg_frequency=("frequency", "mean"),
    avg_spending=("monetary", "mean"),
    avg_order_value=("avg_order_value", "mean")
).round(2)

print("\nPREMIUM SEGMENT CHECK")
print(summary)

print("\nCHECK COMPLETED!")