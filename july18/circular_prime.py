def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = "197"

ok = True
for _ in range(len(n)):
    if not prime(int(n)):
        ok = False
        break
    n = n[1:] + n[0]

print(ok)