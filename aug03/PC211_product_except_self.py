nums = [1, 2, 3, 4]

result = []

for i in range(len(nums)):
    p = 1
    for j in range(len(nums)):
        if i != j:
            p *= nums[j]
    result.append(p)

print(result)