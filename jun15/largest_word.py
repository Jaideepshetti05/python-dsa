sentence = input()

words = sentence.split()

print(max(words, key=len))