# File: count_vowels.py

text = input("Enter text: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)