text = "Programming"
count = sum(1 for c in text.lower() if c in "aeiou")
print(count)