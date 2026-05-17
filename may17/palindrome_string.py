# File: palindrome_string.py

text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")