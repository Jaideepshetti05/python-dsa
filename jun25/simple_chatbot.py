print("Simple ChatBot")
print("Type 'bye' to exit.\n")

while True:

    user = input("You : ").lower()

    if user == "hello":
        print("Bot : Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot : I'm doing great!")

    elif user == "your name":
        print("Bot : My name is PythonBot.")

    elif user == "bye":
        print("Bot : Goodbye!")
        break

    else:
        print("Bot : Sorry, I don't understand.")