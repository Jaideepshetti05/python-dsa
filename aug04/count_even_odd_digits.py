
n = 1234567

even = odd = 0

for d in str(n):
    if int(d) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)