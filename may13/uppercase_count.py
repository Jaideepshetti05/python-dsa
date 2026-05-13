text = input()

count = 0

for ch in text:
    if ch.isupper():
        count += 1

print("Uppercase Letters:", count)