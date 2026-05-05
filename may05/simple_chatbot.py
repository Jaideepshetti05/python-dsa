while True:
    msg = input("You: ").lower()

    if "hello" in msg:
        print("Bot: Hi!")
    elif "bye" in msg:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand")