sentence = input("Enter sentence: ")

words = sentence.split()

largest = max(words, key=len)

print("Largest word:", largest)