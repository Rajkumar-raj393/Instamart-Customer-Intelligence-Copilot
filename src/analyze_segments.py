import pandas as pd

# Load original customer features
features = pd.read_csv(
    "data/processed/customer_features.csv"
)

# Load customer segment labels
segments = pd.read_csv(
    "data/processed/customer_segments.csv"
)

# Combine both datasets
df = features.merge(
    segments[["customer_id", "segment"]],
    on="customer_id"
)

# Display average customer behaviour
summary = df.groupby("segment").agg(
    customers=("customer_id", "count"),
    avg_recency=("recency_days", "mean"),
    avg_frequency=("frequency", "mean"),
    avg_spending=("monetary", "mean")
).round(2)

print("CUSTOMER SEGMENT ANALYSIS")
print("-------------------------")
print(summary)

print("\nSEGMENT ANALYSIS COMPLETED!")