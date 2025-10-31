def facts_chatbot():
    facts = {
        "sun": "The Sun is a star at the center of the solar system.",
        "earth": "Earth is the third planet from the Sun and the only known planet to support life.",
        "moon": "The Moon is Earth's only natural satellite.",
        "water": "Water covers about 71% of Earth's surface.",
        "python": "Python is a popular programming language created by Guido van Rossum.",
        "human": "The human body has 206 bones.",
        "india": "India is the seventh-largest country by land area and the second-most populous country.",
        "ocean": "The Pacific Ocean is the largest and deepest of Earth's oceanic divisions."
    }
    print("🤖 Facts Chatbot: Ask me about something! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("🤖 Chatbot: Goodbye!")
            break
        found = False
        for key in facts:
            if key in user_input:
                print("🤖 Chatbot:", facts[key])
                found = True
                break
        if not found:
            print("🤖 Chatbot: I don't have a fact about that.")

facts_chatbot()
