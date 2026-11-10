import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mock_llm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

POLICY_FOLDER = "data/policies"

documents = []
document_names = []

for filename in os.listdir(POLICY_FOLDER):
    if filename.endswith(".txt"):
        path = os.path.join(POLICY_FOLDER, filename)
        with open(path, "r", encoding="utf-8") as file:
            documents.append(file.read())
            document_names.append(filename)

vectorizer = TfidfVectorizer(stop_words="english")
policy_vectors = vectorizer.fit_transform(documents)


def search_policy(question, top_k=2):
    query_vector = vectorizer.transform([question])
    scores = cosine_similarity(query_vector, policy_vectors)[0]

    best_indices = scores.argsort()[::-1][:top_k]

    results = []
    for index in best_indices:
        if scores[index] > 0:
            results.append(
                f"[{document_names[index]}] {documents[index]}"
            )

    return "\n".join(results)


def ask_policy(question):
    context = search_policy(question)

    messages = [
        {
            "role": "system",
            "content": "You are a POLICY ASSISTANT. Answer only using the supplied policy context. If the answer is not available, say you could not find it."
        },
        {
            "role": "user",
            "content": f"CONTEXT:\n{context}\nQUESTION:\n{question}"
        }
    ]

    response = mock_llm.chat(messages)
    return response.choices[0].message.content


if __name__ == "__main__":
    questions = [
        "How many days do I have to request a refund?",
        "Who approves refunds above INR 1000?",
        "What is the delivery fee for small orders?",
        "How quickly is deducted money returned after payment failure?",
        "What is the favourite colour of the company mascot?"
    ]

    print("\nPOLICY ASSISTANT TEST")

    for question in questions:
        print("\nQuestion:", question)
        print("Answer:", ask_policy(question))

    print("\nPOLICY ASSISTANT TEST COMPLETED!")