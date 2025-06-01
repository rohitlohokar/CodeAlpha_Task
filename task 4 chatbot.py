print("Welcome to chatbot! (Type 'bye' to exit)")

while True:
    user_input = input("you: ").lower()

    if user_input == "hello":
        print("bot: bol be!")
    elif user_input == "how are you":
        print("bot: I'm fine, thanks!")
    elif user_input == "bye":
        print("bot: Goodbye! Have a nice day.")
        break
    else:
        print("bot: Sorry, I didn't understand that.")