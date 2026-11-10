import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load original ticket labels
actual = pd.read_csv(
    "data/processed/tickets_clean.csv"
)

# Load triage predictions
predicted = pd.read_csv(
    "data/processed/ticket_triage_results.csv"
)

# Combine using ticket ID
df = actual[["ticket_id", "true_category"]].merge(
    predicted[["ticket_id", "predicted_category"]],
    on="ticket_id"
)

# Exclude empty tickets labelled as "none"
df = df[df["true_category"] != "none"]

# Evaluate classification
y_true = df["true_category"]
y_pred = df["predicted_category"]

print("TICKET TRIAGE EVALUATION")
print("------------------------")

print("\nTotal evaluated tickets:", len(df))

print("\nAccuracy:", round(
    accuracy_score(y_true, y_pred), 3
))

print("\nClassification Report:")
print(classification_report(
    y_true,
    y_pred,
    zero_division=0
))

print("\nConfusion Matrix:")
print(confusion_matrix(
    y_true,
    y_pred,
    labels=["billing", "delivery", "technical", "fraud"]
))

print("\nEVALUATION COMPLETED!")