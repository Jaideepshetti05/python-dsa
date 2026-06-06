arr = [10, 15, 22, 31, 40]

even = sum(1 for x in arr if x % 2 == 0)
odd = len(arr) - even

print("Even:", even)
print("Odd:", odd)