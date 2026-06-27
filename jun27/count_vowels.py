text = input().lower()

count = sum(1 for c in text if c in "aeiou")

print(count)