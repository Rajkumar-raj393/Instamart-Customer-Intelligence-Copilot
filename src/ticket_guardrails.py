import pandas as pd

# Load triage results
df = pd.read_csv(
    "data/processed/ticket_triage_results.csv"
)

# Apply safety rules
def apply_guardrails(row):
    category = row["predicted_category"]
    text = str(row["text"]).lower()

    # Fraud must go to security immediately
    if category == "fraud":
        return "HIGH", "security_team"

    # Empty or very long tickets need human review
    if (
        not text.strip()
        or len(text.split()) > 300
        or category == "human_review"
    ):
        return "REVIEW", "human_agent"

    return "NORMAL", row["assigned_team"]


# Apply guardrails
results = df.apply(
    apply_guardrails,
    axis=1,
    result_type="expand"
)

df["final_priority"] = results[0]
df["final_assigned_team"] = results[1]

# Save guarded results
df.to_csv(
    "data/processed/ticket_guardrails_results.csv",
    index=False
)

print("TICKET GUARDRAILS COMPLETED")

print("\nFinal priority:")
print(df["final_priority"].value_counts())

print("\nFinal assigned teams:")
print(df["final_assigned_team"].value_counts())

print("\nSaved: data/processed/ticket_guardrails_results.csv")