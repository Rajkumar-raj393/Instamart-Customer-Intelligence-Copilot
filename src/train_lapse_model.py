import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load prepared dataset
df = pd.read_csv(
    "data/processed/lapse_dataset.csv"
)

features = [
    "recency_days",
    "frequency",
    "monetary",
    "avg_order_value"
]

X = df[features]
y = df["will_lapse"]

# Split training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)

print("LAPSE MODEL TRAINING COMPLETED")
print("Accuracy:", round(accuracy_score(y_test, predictions), 3))

print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Save model
joblib.dump(
    model,
    "models/lapse_prediction_model.joblib"
)

print("\nModel saved successfully!")