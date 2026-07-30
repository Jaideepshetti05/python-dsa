arr = [0,5,0,3,8,0,2]

result = [x for x in arr if x!=0]
result.extend([0]*(len(arr)-len(result)))

print(result)