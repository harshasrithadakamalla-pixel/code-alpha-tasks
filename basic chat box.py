
def chatbot():
    print("Chatbot: Hi! I am a simple chatbot.")
    print("Chatbot: You can say hello, ask how are you, or say bye.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

# Start the chatbot
chatbot()