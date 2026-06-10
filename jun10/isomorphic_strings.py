s = "egg"
t = "add"

mapping = {}

for a, b in zip(s, t):
    if a in mapping:
        if mapping[a] != b:
            print(False)
            exit()
    else:
        mapping[a] = b

print(True)