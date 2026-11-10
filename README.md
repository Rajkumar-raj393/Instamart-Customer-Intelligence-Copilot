# Instamart Customer Intelligence & Support Copilot

## Project Overview
This project builds an offline customer intelligence and support copilot for a grocery delivery business.

It covers data cleaning, customer segmentation, lapse prediction, support ticket triage, policy retrieval, and refund automation.

## Technology Stack
- Python
- Pandas and NumPy
- Scikit-learn
- SQLite
- Joblib
- TF-IDF and cosine similarity
- Offline mock LLM

## Part A: Data Foundation
- Cleaned customer, order, product, and ticket datasets.
- Removed duplicate and invalid records.
- Stored cleaned data in SQLite.
- Checked database integrity.
- Performed SQL analysis.

## Part B: Customer Intelligence
- Created RFM customer features.
- Scaled customer features.
- Applied K-Means clustering with 3 segments.
- Trained a Random Forest lapse prediction model.
- Generated customer lapse predictions and a customer intelligence report.

Premium segment was identified using the highest average order value as a proxy.

## Part C: Support Ticket Triage
- Masked customer phone numbers and email addresses.
- Classified tickets into billing, delivery, technical, and fraud categories.
- Applied priority and human-review guardrails.
- Applied response SLAs:
  - Premium customers: 1 hour.
  - Other customers: 24 hours.
  - Fraud security escalation: 2 hours.

Final ticket count: 164.
Fraud tickets: 39.
Human review tickets: 8.

## Part D: Policy Assistant and Refund Agent
- Built TF-IDF policy retrieval.
- Connected the offline mock LLM.
- Created a refund agent using SQLite and tool calls.
- Tested refund eligibility and human escalation for refunds above INR 1000.

## Project Structure
- data/raw: Generated source datasets.
- data/processed: Cleaned datasets and model outputs.
- data/policies: Policy documents.
- src: Python source files.
- models: Trained machine-learning models.
- tests: Project tests.
- generate_data.py: Dataset generator.
- mock_llm.py: Offline LLM simulator.

## How to Run
Install dependencies:

```bash
python -m pip install pandas numpy scikit-learn joblib
```

Generate datasets:

```bash
python generate_data.py
```

Run the project scripts from the project root using Python:

```bash
python src/clean_data.py
python src/clean_orders.py
python src/clean_products.py
python src/clean_tickets.py
python src/build_database.py
python src/customer_features.py
python src/prepare_segmentation.py
python src/customer_segmentation.py
python src/prepare_lapse_data.py
python src/train_lapse_model.py
python src/predict_lapse.py
python src/mask_ticket_pii.py
python src/ticket_triage.py
python src/ticket_guardrails.py
python src/finalize_ticket_sla.py
python src/policy_retrieval.py
python src/evaluate_policy.py
python src/refund_agent.py
```

## Notes
This project uses synthetic data and an offline mock LLM. Results are for educational demonstration and are not production performance claims.