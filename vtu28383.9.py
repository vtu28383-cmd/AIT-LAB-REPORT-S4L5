import random

def chatbot_response(user_input):
    user_input = user_input.lower()
    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    responses = ["I'm fine, thank you!", "Doing great!", "All good! How about you?"]
    if any(greet in user_input for greet in greetings):
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help you?"])
    elif "how are you" in user_input:
        return random.choice(responses)
    elif "name" in user_input:
        return "I'm ChatBot, your virtual assistant."
    elif "n queen" in user_input or "n queens" in user_input:
        return "The N-Queens problem is a classic backtracking problem in chess!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure I understand. Can you rephrase?"

def chat():
    print("🤖 ChatBot: Hello! I'm your assistant. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 ChatBot: Goodbye!")
            break
        print("🤖 ChatBot:", chatbot_response(user_input))

if __name__ == "__main__":
    chat()
