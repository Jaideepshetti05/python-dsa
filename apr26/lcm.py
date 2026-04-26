a, b = 12, 18
max_val = max(a, b)
while True:
    if max_val % a == 0 and max_val % b == 0:
        print(max_val)
        break
    max_val += 1