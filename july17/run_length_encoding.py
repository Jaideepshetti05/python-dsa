s = "aaabbcccc"

i = 0
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
        i += 1
    print(s[i], count, end="")
    i += 1