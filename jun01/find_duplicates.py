numbers = [1, 2, 3, 2, 4, 5, 1]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    seen.add(num)

print("Duplicates:", duplicates)