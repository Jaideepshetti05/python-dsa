# File: sum_even_numbers.py
n = int(input())

sum_even = 0

for i in range(2, n + 1, 2):
    sum_even += i

print(sum_even)