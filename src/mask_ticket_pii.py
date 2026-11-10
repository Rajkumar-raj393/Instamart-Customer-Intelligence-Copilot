import pandas as pd
import re

# Load cleaned support tickets
df = pd.read_csv(
    "data/processed/tickets_clean.csv"
)

# Replace missing ticket text
df["text"] = df["text"].fillna("").astype(str)

# Mask email addresses
def mask_email(text):
    return re.sub(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        "[EMAIL_MASKED]",
        text
    )

# Mask phone numbers
def mask_phone(text):
    return re.sub(
        r"(?<!\d)(?:\+91[\s-]?)?[6-9]\d{9}(?!\d)",
        "[PHONE_MASKED]",
        text
    )

# Apply privacy masking
df["text"] = df["text"].apply(mask_email)
df["text"] = df["text"].apply(mask_phone)

# Save masked tickets
df.to_csv(
    "data/processed/tickets_masked.csv",
    index=False
)

print("CUSTOMER PRIVACY MASKING COMPLETED")
print("Total tickets:", len(df))
print("Email and phone masking applied.")
print("Saved: data/processed/tickets_masked.csv")