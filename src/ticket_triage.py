import pandas as pd

# Load privacy-protected tickets
tickets = pd.read_csv(
    "data/processed/tickets_masked.csv"
)

# Load customer segments from Part B
segments = pd.read_csv(
    "data/processed/customer_segments.csv"
)

# Attach customer segment information
df = tickets.merge(
    segments[["customer_id", "segment"]],
    on="customer_id",
    how="left"
)

# Classify ticket text using simple rules
def classify_ticket(text):
    text = str(text).lower()

    if not text.strip():
        return "human_review"

    if any(word in text for word in [
        "fraud", "unauthorized", "hacked"
    ]):
        return "fraud"

    if any(word in text for word in [
        "charged", "refund", "invoice",
        "payment", "bill", "deducted"
    ]):
        return "billing"

    if any(word in text for word in [
        "delivery", "rider", "late",
        "arrived", "delivered"
    ]):
        return "delivery"

    if any(word in text for word in [
        "app", "login", "otp", "crashes",
        "error", "freezes"
    ]):
        return "technical"

    return "human_review"


# Classify all tickets
df["predicted_category"] = df["text"].apply(
    classify_ticket
)

# Assign priority
df["priority"] = df["predicted_category"].apply(
    lambda category: (
        "high" if category == "fraud"
        else "review" if category == "human_review"
        else "normal"
    )
)

# Assign support team
team_mapping = {
    "fraud": "security_team",
    "billing": "billing_support",
    "delivery": "delivery_support",
    "technical": "technical_support",
    "human_review": "human_agent"
}

df["assigned_team"] = df[
    "predicted_category"
].map(team_mapping)

# Save triage results
df.to_csv(
    "data/processed/ticket_triage_results.csv",
    index=False
)

print("TICKET TRIAGE COMPLETED")

print("\nTicket categories:")
print(df["predicted_category"].value_counts())

print("\nPriority distribution:")
print(df["priority"].value_counts())

print("\nAssigned teams:")
print(df["assigned_team"].value_counts())

print("\nSaved: data/processed/ticket_triage_results.csv")