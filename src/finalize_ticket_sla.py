import os
import pandas as pd

INPUT = "data/processed/ticket_guardrails_results.csv"
CUSTOMER_REPORT = "data/processed/customer_intelligence_report.csv"
OUTPUT = "data/processed/ticket_sla_final.csv"

df = pd.read_csv(INPUT)

# Identify the Premium segment using the highest average order value.
premium_segment = None

if os.path.exists(CUSTOMER_REPORT):
    customers = pd.read_csv(CUSTOMER_REPORT)

    if "segment" in customers.columns and "avg_order_value" in customers.columns:
        segment_values = customers.groupby("segment")["avg_order_value"].mean()
        if not segment_values.empty:
            premium_segment = segment_values.idxmax()

# Set customer response SLA.
df["customer_response_sla_hours"] = 24

if premium_segment is not None:
    df.loc[
        df["segment"].astype(str) == str(premium_segment),
        "customer_response_sla_hours"
    ] = 1

# Fraud tickets must be escalated to Security within 2 hours.
df["security_escalation_sla_hours"] = None
fraud_mask = df["predicted_category"].astype(str).str.lower() == "fraud"
df.loc[fraud_mask, "security_escalation_sla_hours"] = 2

# Ensure fraud tickets retain high priority and Security assignment.
df.loc[fraud_mask, "final_priority"] = "HIGH"
df.loc[fraud_mask, "final_assigned_team"] = "security_team"

# Keep empty and very long tickets for human review.
review_mask = df["text_empty"].fillna(False) | df["text_too_long"].fillna(False)
df.loc[review_mask, "final_priority"] = "REVIEW"
df.loc[review_mask, "final_assigned_team"] = "human_agent"

df.to_csv(OUTPUT, index=False)

print("TICKET SLA FINALIZATION SUCCESSFUL")
print("Total tickets:", len(df))
print("Premium segment:", premium_segment)
print("Fraud tickets:", int(fraud_mask.sum()))
print("Human review tickets:", int(review_mask.sum()))
print("Output saved:", OUTPUT)
print("\nSLA summary:")
print(df.groupby("customer_response_sla_hours").size())
print("\nFinal priority summary:")
print(df["final_priority"].value_counts())