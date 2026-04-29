# Task 4: Basic Chatbot

print("Chatbot Activated! (type 'Hello' to exit)\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I'm fine, thank you!")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand that")