arr=[1,0,5,0,7,2,0]

result=[x for x in arr if x!=0]
result.extend([0]*(len(arr)-len(result)))

print(result)