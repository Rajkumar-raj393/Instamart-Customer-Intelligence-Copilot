import pandas as pd
import joblib

# Load customer data
df = pd.read_csv(
    "data/processed/lapse_dataset.csv"
)

# Load trained model
model = joblib.load(
    "models/lapse_prediction_model.joblib"
)

# Select features
features = [
    "recency_days",
    "frequency",
    "monetary",
    "avg_order_value"
]

X = df[features]

# Generate predictions
df["predicted_lapse"] = model.predict(X)

df["lapse_probability"] = model.predict_proba(X)[:, 1]

# Save predictions
df.to_csv(
    "data/processed/lapse_predictions.csv",
    index=False
)

print("CUSTOMER LAPSE PREDICTIONS COMPLETED")
print("\nPrediction counts:")
print(df["predicted_lapse"].value_counts())

print("\nPrediction preview:")
print(
    df[[
        "customer_id",
        "predicted_lapse",
        "lapse_probability"
    ]].head(10)
)

print("\nSaved: data/processed/lapse_predictions.csv")