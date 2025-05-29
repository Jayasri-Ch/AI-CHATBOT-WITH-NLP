import re
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Memory to store conversation history
conversation_log = []

# Preprocessing without nltk punkt
def preprocess(text):
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)  # regex-based tokenizer
    return ' '.join(tokens)

# Chatbot logic
def chatbot_response(user_input):
    # Add user's message to conversation log
    conversation_log.append(preprocess(user_input))

    # If not enough history, return a generic response
    if len(conversation_log) < 2:
        return random.choice([
            "Tell me more.",
            "Interesting! What else?",
            "Why do you say that?",
            "I'm listening..."
        ])

    # Vectorize all previous inputs
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(conversation_log)

    # Compare last input with previous ones
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    most_similar_index = similarity.argmax()
    confidence = similarity[0, most_similar_index]

    if confidence > 0.3:
        return "You mentioned something similar earlier. Let's explore that more."
    else:
        return random.choice([
            "That's new! Let's dive into it.",
            "Fascinating. Please continue.",
            "Could you explain that a bit more?",
            "Okay. I'm here to understand."
        ])

# Main chat loop
print("🤖 Chatbot: Hello! I'm here to chat.")
while True:
    user_input = input("🧑 You: ")
    if user_input.strip().lower() == "exit":
        print("🤖 Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("🤖 Chatbot:", response)
