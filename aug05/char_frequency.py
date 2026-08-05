text = "banana"

freq = {}

for c in text:
    freq[c] = freq.get(c,0)+1

print(freq)