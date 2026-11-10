import csv
from policy_retrieval import ask_policy

EVALUATION_FILE = "data/raw/policy_eval.csv"

correct = 0
total = 0

print("\nPOLICY EVALUATION STARTED")

with open(EVALUATION_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("Columns:", reader.fieldnames)

    for row in reader:
        question = row.get("question", "")

        if not question:
            continue

        answer = ask_policy(question)

        total += 1

        print("\nQuestion:", question)
        print("Answer:", answer)

print("\nTotal questions tested:", total)
print("POLICY EVALUATION COMPLETED!")