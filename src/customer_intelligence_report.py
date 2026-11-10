import pandas as pd

# Load customer information
customers = pd.read_csv(
    "data/processed/customer_features.csv"
)

# Load customer segments
segments = pd.read_csv(
    "data/processed/customer_segments.csv"
)

# Load lapse predictions
predictions = pd.read_csv(
    "data/processed/lapse_predictions.csv"
)

# Combine all information
report = customers.merge(
    segments[["customer_id", "segment"]],
    on="customer_id"
)

report = report.merge(
    predictions[[
        "customer_id",
        "predicted_lapse",
        "lapse_probability"
    ]],
    on="customer_id"
)

# Create readable status
report["customer_status"] = report[
    "predicted_lapse"
].map({
    0: "Active",
    1: "At Risk"
})

# Save final report
report.to_csv(
    "data/processed/customer_intelligence_report.csv",
    index=False
)

print("CUSTOMER INTELLIGENCE REPORT CREATED")
print("\nCustomer status:")
print(report["customer_status"].value_counts())

print("\nSegment summary:")
print(
    report.groupby("segment").agg(
        customers=("customer_id", "count"),
        average_spending=("monetary", "mean"),
        at_risk=("predicted_lapse", "sum")
    ).round(2)
)

print("\nReport saved successfully!")