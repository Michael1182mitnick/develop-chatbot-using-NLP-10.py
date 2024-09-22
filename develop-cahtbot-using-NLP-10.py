# Install spaCy:
# pip install spacy
# python -m spacy download en_core_web_sm
# Build a rule-based or machine learning-based chatbot that can answer user queries. Use NLP libraries like spaCy or NLTK to process and understand text.
# Rule-Based Chatbot Code:

import spacy

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Simple rule-based response dictionary for predefined intents
INTENTS = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "farewell": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thanks", "thank you"],
    "weather": ["weather", "rain", "sunny", "cloudy", "windy", "forecast"]
}

RESPONSES = {
    "greeting": "Hello! How can I assist you today?",
    "farewell": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "weather": "I can't give a weather report at the moment, but you can check your local forecast!"
}

# Function to find intent in user input


def get_intent(user_input):
    # Process the input text using spaCy
    doc = nlp(user_input.lower())

    # Extract the intent based on keyword matching
    for token in doc:
        for intent, keywords in INTENTS.items():
            if token.text in keywords:
                return intent
    return None

# Chatbot function to get response


def chatbot(user_input):
    intent = get_intent(user_input)
    if intent in RESPONSES:
        return RESPONSES[intent]
    else:
        return "Sorry, I didn't understand that."


# Main chatbot loop
if __name__ == "__main__":
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot(user_input)
        print(f"Chatbot: {response}")
