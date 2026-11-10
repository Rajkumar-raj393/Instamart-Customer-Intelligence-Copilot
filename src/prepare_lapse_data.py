import pandas as pd

# Load customer features
df = pd.read_csv(
    "data/processed/customer_features.csv"
)

# Create lapse label
# 1 = Customer inactive for more than 60 days
# 0 = Customer active within 60 days

df["will_lapse"] = (
    df["recency_days"] > 60
).astype(int)

# Select model features
features = [
    "recency_days",
    "frequency",
    "monetary",
    "avg_order_value"
]

X = df[features].fillna(0)
y = df["will_lapse"]

# Save prepared dataset
prepared = X.copy()
prepared["customer_id"] = df["customer_id"]
prepared["will_lapse"] = y

prepared.to_csv(
    "data/processed/lapse_dataset.csv",
    index=False
)

print("LAPSE DATASET CREATED")
print("\nCustomer counts:")
print(y.value_counts())

print("\nSaved: data/processed/lapse_dataset.csv")