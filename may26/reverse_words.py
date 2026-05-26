# File: reverse_words.py
text = input()

words = text.split()

print(" ".join(words[::-1]))