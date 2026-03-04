from collections import Counter

s = "programming"
count = Counter(s)

for c in s:
    if count[c] == 1:
        print("First non repeating:", c)
        break