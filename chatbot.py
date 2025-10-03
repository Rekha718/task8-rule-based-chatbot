print("🤖 Hello! I am ChatBot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()  # Get user input and convert to lowercase
    
    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")
        
    elif user_input == "how are you":
        print("Bot: I'm a bot, but I'm doing great! How about you?")
        
    elif user_input == "what is your name":
        print("Bot: I am ChatBot, your friendly assistant.")
        
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break  # Exit the loop
        
    else:
        print("Bot: Sorry, I didn't understand that.")
