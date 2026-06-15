text = input().lower()

count = sum(1 for ch in text if ch in "aeiou")

print(count)