import string

text = "The quick brown fox jumps over the lazy dog"

if set(string.ascii_lowercase) <= set(text.lower()):
    print("Pangram")
else:
    print("Not Pangram")