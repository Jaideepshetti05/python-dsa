nums = [1,2,3,4,5]
k = 2

k %= len(nums)

result = nums[k:] + nums[:k]

print(result)