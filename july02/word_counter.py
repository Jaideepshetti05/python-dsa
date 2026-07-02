with open("sample.txt") as f:
    words = 0
    for line in f:
        words += len(line.split())

print(words)