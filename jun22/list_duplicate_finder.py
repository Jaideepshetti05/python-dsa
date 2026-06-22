data = [1,2,3,2,5,1]

duplicates = set([x for x in data if data.count(x) > 1])

print(duplicates)