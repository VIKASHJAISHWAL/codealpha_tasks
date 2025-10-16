def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks for asking! How about you?")
        elif user_input in ["i'm fine", "i am fine", "fine"]:
            print("Chatbot: That's great to hear!")
        elif user_input == "what is your name":
            print("Chatbot: I'm CodeAlpha Chatbot")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

chatbot()