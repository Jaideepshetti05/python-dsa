nums = list(map(int, input().split()))

nums = list(set(nums))
nums.sort()

print(nums[-2])