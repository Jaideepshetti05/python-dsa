nums = [1, 2, 3, 4, 5]
k = 2

for _ in range(k):
    nums.insert(0, nums.pop())

print(nums)