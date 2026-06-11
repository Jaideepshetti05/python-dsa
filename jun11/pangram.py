sentence = input("Enter sentence: ").lower()

alphabet = set("abcdefghijklmnopqrstuvwxyz")

if alphabet <= set(sentence):
    print("Pangram")
else:
    print("Not Pangram")