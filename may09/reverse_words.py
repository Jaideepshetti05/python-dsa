text = input("Enter sentence: ")

words = text.split()

reversed_sentence = " ".join(words[::-1])

print(reversed_sentence)