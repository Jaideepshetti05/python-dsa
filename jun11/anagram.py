a = input("First string: ")
b = input("Second string: ")

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")