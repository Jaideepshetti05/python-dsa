arr = [1,2,3,2,4]
seen = set()

for x in arr:
    if x in seen:
        print("Duplicate:", x)
    seen.add(x)