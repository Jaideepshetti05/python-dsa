import string

text = "The quick brown fox jumps over the lazy dog"

letters = set(text.lower())

print(all(ch in letters for ch in string.ascii_lowercase))