sentence = input("Enter sentence: ")

words = sentence.split()

for word in words:
    print(word[::-1], end=" ")