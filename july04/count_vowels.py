text = "Artificial Intelligence"

count = sum(ch.lower() in "aeiou" for ch in text)

print(count)