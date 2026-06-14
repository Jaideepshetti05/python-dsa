text = "Artificial Intelligence"

result = ''.join(ch for ch in text if ch.lower() not in "aeiou")

print(result)