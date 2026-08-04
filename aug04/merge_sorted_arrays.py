a = [1,3,5]
b = [2,4,6]

i = j = 0
res = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

res.extend(a[i:])
res.extend(b[j:])

print(res)