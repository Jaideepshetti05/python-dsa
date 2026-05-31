text = "Hello Python World"

result = " ".join(word[::-1] for word in text.split())

print(result)