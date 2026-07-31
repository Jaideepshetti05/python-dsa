matrix=[[4,8],[15,2]]

nums=[n for row in matrix for n in row]

nums=sorted(set(nums))

print(nums[-2])